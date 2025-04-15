# Utilise une image Python officielle avec la bonne version
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances en premier pour tirer parti du cache Docker
COPY requirements.txt .

# Installer les dépendances système nécessaires (optionnel mais conseillé pour pymongo/motor et cryptography)
RUN apt-get update && apt-get install -y gcc libpq-dev libssl-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get remove -y gcc && \
    apt-get autoremove -y && \
    apt-get clean

# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel FastAPI sera disponible
EXPOSE 8000

# Lancer l'application FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
