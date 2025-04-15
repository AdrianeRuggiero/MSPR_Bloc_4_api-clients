# Utilisation de l'image Python 3.11 comme image de base
FROM python:3.11-slim

# Définir le répertoire de travail à /app
WORKDIR /app

# Copier le fichier des dépendances requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python (y compris FastAPI, Uvicorn, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application dans le conteneur
COPY . .

# Exposer le port 8000 pour l'application FastAPI
EXPOSE 8000

# Définir la commande de démarrage pour lancer l'application FastAPI avec Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
