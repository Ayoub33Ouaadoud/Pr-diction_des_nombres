
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Input,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

# 1. Charger les données MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("Images d'entraînement :", X_train.shape)
print("Images de test :", X_test.shape)

# 2. Normaliser les pixels entre 0 et 1
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# 3. Ajouter le canal des images en niveaux de gris
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

# 4. Construire le CNN
model = Sequential([
    Input(shape=(28, 28, 1)),
    Conv2D(32, kernel_size=(3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.3),
    Dense(10, activation="softmax")
])

# 5. Configurer l'entraînement
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# 6. Entraîner le modèle
history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=128,
    validation_split=0.1
)

# 7. Évaluer le modèle sur les données de test
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print(f"Précision sur le test : {accuracy * 100:.2f} %")
print(f"Perte sur le test : {loss:.4f}")

# 8. Créer le dossier models
dossier = Path("models")
dossier.mkdir(exist_ok=True)

# 9. Sauvegarder le modèle entraîné
chemin = dossier / "mnist_model.keras"
model.save(chemin)

print(f"Modèle sauvegardé ici : {chemin.resolve()}")

# 10. Afficher quelques prédictions
probabilites = model.predict(X_test[:10], verbose=0)
predictions = np.argmax(probabilites, axis=1)

plt.figure(figsize=(12, 5))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[i].squeeze(), cmap="gray")
    plt.title(f"Réel : {y_test[i]} | Prédit : {predictions[i]}")
    plt.axis("off")

plt.tight_layout()
plt.show()
