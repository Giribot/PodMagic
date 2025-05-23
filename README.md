# 🎧 PodMagic — Téléchargeur Intelligent de Podcasts Radio France

PodMagic est un téléchargeur de podcasts Radio France écrit en Python. Il permet de contrôler le nombre d'épisodes à récupérer et crée automatiquement une archive ZIP contenant les fichiers.  
> ⚠️ Nécessite un environnement Python installé au préalable.

---

## ✨ Fonctionnalités

- Interface web interactive avec **Gradio**
- Détection automatique des épisodes **MP3**
- Contrôle précis du **nombre d’épisodes** à télécharger
- **Numérotation automatique** des fichiers (`01_`, `02_`, …)
- Création d’une **archive ZIP optimisée**
- **Compatibilité multi-plateforme** : Windows / Linux / macOS
- **Déploiement 1-clic** sur Hugging Face Spaces

---

## 🛠️ Installation

Cloner le dépôt :

```bash
git clone https://github.com/Giribot/PodMagic.git
cd PodMagic
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer l’application :

```bash
python app.py
```

---

## 🖥️ Utilisation

1. Entrer l’URL de la série podcast (ex. : *La nuit du Merveilleux Scientifique*) :

   ```
   https://www.radiofrance.fr/franceculture/podcasts/serie-la-nuit-du-merveilleux-scientifique
   ```

2. Spécifier le **nombre d’épisodes** à télécharger (`0` = tous)

   > Exemple : pour 11 épisodes, entrer `11`.  
   > ⚠️ Si vous mettez `0`, le script peut télécharger d'autres podcasts non liés (présents dans le code source de la page). C'est une limitation connue.

3. Cliquer sur **Télécharger**

---

## 🧰 Technologies Clés

- **Gradio** : interface utilisateur web
- **BeautifulSoup** : parsing HTML
- **Requests** : gestion des requêtes HTTP
- **Zipfile** : compression des fichiers

---

## 🌐 Déploiement

### Sur Hugging Face Spaces

1. Créer un nouveau *Space*
2. Choisir le **SDK Gradio**
3. Copier le contenu de `app.py`
4. Ajouter les dépendances dans `requirements.txt`

### Avec Docker

```dockerfile
FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

## ⚠️ Notes Importantes

- Compatible uniquement avec **radiofrance.fr**
- Nécessite une URL **complète** de série podcast
- Les noms de fichiers sont basés sur les **URLs**
- Peut nécessiter des ajustements en cas de mise à jour du site Radio France

---

## 🤝 Contribution

Les contributions sont les bienvenues !  
N’hésitez pas à proposer des améliorations ou à signaler des bugs via *issues* ou *pull requests*.

---