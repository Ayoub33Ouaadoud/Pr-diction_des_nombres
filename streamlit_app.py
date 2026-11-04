
from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model


# 1. Configurer la page
st.set_page_config(
    page_title="Reconnaissance de chiffres",
    page_icon="🔢",
    layout="centered"
)


# 2. Localiser le modèle
MODEL_PATH = Path(__file__).parent / "models" / "mnist_model.keras"


# 3. Charger le modèle une seule fois
@st.cache_resource
def charger_modele():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Le modèle est introuvable : {MODEL_PATH}"
        )

    return load_model(MODEL_PATH)


# 4. Préparer l'image pour le CNN
def preparer_image(image):
    # Convertir en niveaux de gris
    image = ImageOps.grayscale(image)

    # Redimensionner en 28 x 28 pixels
    image = image.resize((28, 28))

    # Inverser les couleurs : chiffre clair sur fond sombre
    image = ImageOps.invert(image)

    # Convertir l'image en tableau de nombres
    tableau = np.asarray(image, dtype=np.float32)

    # Normaliser les pixels entre 0 et 1
    tableau = tableau / 255.0

    # Ajouter la dimension du canal
    tableau = np.expand_dims(tableau, axis=-1)

    # Ajouter la dimension du lot (batch)
    tableau = np.expand_dims(tableau, axis=0)

    return tableau


# 5. Construire l'interface
st.title("🔢 Reconnaissance de chiffres manuscrits")

st.write(
    "Chargez une image contenant un chiffre manuscrit "
    "entre 0 et 9, puis lancez la prédiction."
)

fichier = st.file_uploader(
    "Sélectionner une image",
    type=["png", "jpg", "jpeg"]
)


# 6. Traiter l'image envoyée
if fichier is not None:
    image = Image.open(fichier).convert("RGB")

    st.subheader("Image sélectionnée")
    st.image(
        image,
        caption="Image fournie",
        width=250
    )

    if st.button("Prédire le chiffre"):
        try:
            # Charger le modèle
            model = charger_modele()

            # Préparer l'image
            entree = preparer_image(image)

            # Effectuer la prédiction
            scores = model.predict(entree, verbose=0)[0]

            # Identifier le chiffre le plus probable
            chiffre = int(np.argmax(scores))
            confiance = float(scores[chiffre])

            # Afficher le résultat
            st.success(f"Chiffre prédit : {chiffre}")

            st.metric(
                "Score du chiffre prédit",
                f"{confiance * 100:.2f} %"
            )

            # Afficher les scores des dix classes
            st.subheader("Scores des dix classes")

            st.bar_chart({
                "Score": scores
            })

        except Exception as erreur:
            st.error(
                f"Une erreur est survenue : {erreur}"
            )
