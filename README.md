Téléchargeur intelligent de podcasts Radio France avec contrôle du nombre d'épisodes et création d'archive ZIP en Python
(nécessité d'avoir un environnement Python installé au préalable.)

## ✨ Fonctionnalités

- **Interface Web Interactive** avec Gradio
- **Détection Automatique** des épisodes MP3
- **Contrôle Précis** du nombre d'épisodes à télécharger
- **Numérotation Automatique** des fichiers (01_, 02_, ...)
- **Création d'Archive ZIP** optimisée
- **Compatibilité Multi-Plateforme** (Windows/Linux/Mac)
- **Hébergement 1-Clic** sur Hugging Face Spaces

## 🛠️ Installation

1. **Cloner le dépôt** :
```bash
git https://github.com/Giribot/PodMagic.git
cd Podmagic

1.Installer les dépendances :

```bash
pip install -r requirements.txt

3- Lancer l'application :

```bash
python app.py


🖥️ Utilisation
Entrer l'URL de la série podcast (ex : série La nuit du Merveilleux Scientifique)

https://www.radiofrance.fr/franceculture/podcasts/serie-la-nuit-du-merveilleux-scientifique
Spécifier le nombre d'épisodes (0 = tous)
Ici, il y a 11 épisodes: on rentrera le chiffre 11 pour télécharger tous les épisodes de cette série....
Si vous mettez 0, le script a tendance à télécharger d'autres podcasts qui n'ont rien à voir avec le podcast choisi mais qui sont présent dans le code source de la page ! (je n'ai pas trouvé comment remédier à ça pour le moment: pas trop le temps)
Cliquer sur "Télécharger"


Technologies Clés
Gradio : Interface utilisateur Web

BeautifulSoup : Parsing HTML

Requests : Gestion des requêtes HTTP

Zipfile : Compression des fichiers

🌐 Déploiement
Sur Hugging Face Spaces
Créer un nouveau Space

Choisir Gradio SDK

Copier le code de app.py

Ajouter les dépendances dans requirements.txt

Avec Docker
dockerfile
FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
⚠️ Notes Importantes
Uniquement compatible avec radiofrance.fr

Nécessite une URL de série podcast complète

Les noms de fichiers sont basés sur les URLs

Peut nécessiter des ajustements en cas de mise à jour du site

🤝 Contribution
Les contributions sont les bienvenues !
