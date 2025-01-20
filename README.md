# TP KANTAR

Ce repository contient le projet en lien avec le TP d'extraction de connaissances dans le cadre la majeure SCIA 2025 d'EPITA.

## Auteurs

Samy Amine : samy.amine@epita.fr
Emile Merle : emile.merle@epita.fr
Julien Schaffauser : julien.schaffauser@epita.fr

## Installation

Créer et activer un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate
```

Installer les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

## Architecture

Le projet est structuré comme suit :

```bash
./
├── data/
│   ├── fic_epita_kantar_codes.csv
│   ├── fic_epita_kantar_labels.csv
│   ├── orange.csv # Généré par la partie 1
│   └── vert.csv # Généré par la partie 1
├── Partie_1/
│   ├── clustering_orange.ipynb
│   └── clustering_vert.ipynb
├── Partie_2/
│   ├── classification_orange.ipynb
│   └── classification_vert.ipynb
├── Partie_3/
│   ├── cross_classification_orange.ipynb
│   └── cross_classification_vert.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```