from pathlib import Path
from tensorflow.keras.models import load_model
chemin = Path("models") / "mnist_model.keras"
model = load_model(chemin)

print("Modèle chargé avec succès !")
print("Forme des entrées :", model.input_shape)
print("Forme des sorties :", model.output_shape)