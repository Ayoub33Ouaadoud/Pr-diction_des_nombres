from docx import Document
from datetime import datetime


def ajouter_section(document, titre, texte, liste_items=None):
    document.add_heading(titre, level=1)
    document.add_paragraph(texte)
    if liste_items:
        for item in liste_items:
            document.add_paragraph(item, style='List Bullet')


doc = Document()
doc.add_heading('Compte rendu de projet', 0)
doc.add_paragraph('Reconnaissance de chiffres manuscrits via un réseau de neurones CNN')
doc.add_paragraph(f"Date : {datetime.now().strftime('%d/%m/%Y')}")
doc.add_paragraph('Nom du projet : Application intelligente de reconnaissance de chiffres manuscrits')
doc.add_paragraph()

ajouter_section(
    doc,
    '1. Contexte et objectif',
    "Ce projet consiste à développer un système capable de reconnaître des chiffres manuscrits de 0 à 9 à partir d'images numériques. L'objectif principal est de démontrer l'efficacité des réseaux de neurones convolutifs (CNN) dans la classification d'images et de proposer une interface simple pour tester le modèle en temps réel.",
)

ajouter_section(
    doc,
    '2. Description du système',
    'Le projet est structuré autour de deux éléments principaux :',
    [
        'Le fichier atelier1_mnist.py : il charge le jeu de données MNIST, construit le modèle CNN, l’entraîne et enregistre le modèle entraîné dans le dossier models.',
        'Le fichier streamlit_app.py : il permet d’importer une image et de lancer une prédiction avec l’interface utilisateur Streamlit.',
        'Le modèle sauvegardé : models/mnist_model.keras',
    ],
)

ajouter_section(
    doc,
    '3. Architecture du modèle',
    'Le modèle est un réseau de neurones convolutif (CNN) composé de plusieurs couches :',
    [
        'Couches de convolution avec activation ReLU pour extraire les caractéristiques visuelles.',
        'Couches de pooling pour réduire la dimension des cartes de caractéristiques.',
        'Une couche Flatten pour transformer les cartes en vecteur.',
        'Une couche dense avec activation ReLU pour la classification finale.',
        'Une couche de sortie softmax avec 10 classes correspondant aux chiffres 0 à 9.',
    ],
)

ajouter_section(
    doc,
    '4. Données et préparation',
    "Le jeu de données utilisé est MNIST, un standard d'IA pour la reconnaissance de chiffres manuscrits. Les images sont converties en niveaux de gris, redimensionnées et normalisées entre 0 et 1 afin d'améliorer la convergence du modèle pendant l'entraînement.",
)

ajouter_section(
    doc,
    '5. Fonctionnement de l’application',
    "L'application permet à l'utilisateur de télécharger une image contenant un chiffre manuscrit. Cette image est ensuite préparée selon les mêmes étapes que celles des données d'apprentissage, puis le modèle calcule les probabilités pour chaque classe. La classe ayant la probabilité la plus élevée est affichée comme résultat, avec un score de confiance associé.",
)

ajouter_section(
    doc,
    '6. Résultats et observations',
    "Le projet montre que les CNN sont particulièrement adaptés à la reconnaissance d'images. L'utilisation de l'interface Streamlit rend le système accessible et facile à tester, même pour un utilisateur non expert. Cela confirme la valeur des modèles d'apprentissage profond pour des tâches de classification visuelle.",
)

ajouter_section(
    doc,
    '7. Conclusion',
    "Ce projet a permis de mettre en place un système complet de reconnaissance de chiffres manuscrits, du prétraitement des images jusqu'à l'intégration dans une application Web. Les résultats obtenus démontrent la pertinence de l'approche utilisée et ouvrent la voie à des améliorations supplémentaires, comme la gestion de chiffres écrits plus complexes ou la mise en place d'une base de données d'exemples supplémentaires.",
)

doc.add_paragraph()
doc.add_paragraph('Responsable du projet : ........................................................')

doc.save('compte_rendu_maitre.docx')
print('Fichier Word généré : compte_rendu_maitre.docx')
