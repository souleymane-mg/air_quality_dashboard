# Air Quality Dashboard

Ce projet est un tableau de bord interactif pour visualiser en temps réel la qualité de l'air et la météo dans différentes régions, basé sur Streamlit et Plotly.

## Prérequis
- Python 3.8 ou supérieur (idéalement 3.10 pour la compatibilité)
- Accès à une clé API OpenWeather (https://openweathermap.org/api)

## Installation

1. **Cloner le dépôt**
```bash
git clone <url-du-repo-github>
cd air_quality_dashboard
```

2. **Créer et activer un environnement virtuel**
- Sous Windows :
```bash
python -m venv .venv
.venv\Scripts\activate
```
- Sous Mac/Linux :
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer la clé API**
- Ouvrir le fichier `.env.example` à la racine du projet.
- Remplacer le texte `votre_clé_api_ici` par votre propre clé API OpenWeather.
- Renommer le fichier `.env.example` en `.env`.

## Lancement de l'application

```bash
streamlit run streamlit_app.py
```

L'application sera accessible à l'adresse indiquée dans le terminal (par défaut http://localhost:8501).

## Dépendances principales
- streamlit
- plotly
- pandas
- python-dotenv
- streamlit-autorefresh

## Conseils
- Ne partagez jamais votre fichier `.env` ou votre clé API sur un dépôt public.
- Si vous modifiez la structure des régions ou ajoutez des fonctionnalités, pensez à mettre à jour ce README.

## Auteur
- Votre nom ici 