import gradio as gr
import requests
import re
import os
import zipfile
import tempfile
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def process_url(url, num_episodes):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.radiofrance.fr/'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        return None, f"Erreur : {str(e)}"

    soup = BeautifulSoup(response.text, 'html.parser')
    mp3_links = []

    # Extraction des liens MP3
    scripts = soup.find_all('script', type='application/ld+json')
    for script in scripts:
        if script.string:
            matches = re.findall(r'"contentUrl"\s*:\s*"([^"]+?\.mp3)', script.string)
            for match in matches:
                full_url = urljoin(url, match.split('?')[0])
                if full_url not in mp3_links:
                    mp3_links.append(full_url)

    # Fallback si nécessaire
    if not mp3_links:
        matches = re.findall(r'(https?://media\.radiofrance-podcast\.net[^\s"\']+?\.mp3)', response.text)
        mp3_links = list(dict.fromkeys(matches))

    # Application du nombre d'épisodes demandé
    try:
        num_episodes = int(num_episodes)
        if num_episodes > 0:
            mp3_links = mp3_links[:num_episodes]
    except:
        pass  # Si valeur invalide, on prend tout

    if not mp3_links:
        return None, "Aucun épisode trouvé"

    # Téléchargement
    temp_dir = tempfile.mkdtemp()
    filenames = []
    
    for idx, mp3_url in enumerate(mp3_links, 1):
        try:
            filename = f"{idx:02d}_{os.path.basename(mp3_url)}"
            filepath = os.path.join(temp_dir, filename)
            
            with requests.get(mp3_url, headers=headers, stream=True) as r:
                r.raise_for_status()
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            filenames.append(filepath)
        except Exception:
            continue

    if not filenames:
        return None, "Échec du téléchargement"

    # Création du ZIP
    zip_path = os.path.join(temp_dir, 'podcast.zip')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in filenames:
            zipf.write(file, arcname=os.path.basename(file))

    return zip_path, None

def download_podcast(url, num_episodes):
    zip_path, error = process_url(url, num_episodes)
    if error:
        raise gr.Error(error)
    return zip_path

with gr.Blocks() as app:
    gr.Markdown("## 🎧 Téléchargeur Radio France - Contrôle des épisodes")
    
    with gr.Row():
        url_input = gr.Textbox(
            label="URL du podcast",
            placeholder="Ex: https://www.radiofrance.fr/...",
            max_lines=1
        )
        num_input = gr.Number(
            label="Nombre d'épisodes (0 = tous)",
            value=0,
            minimum=0,
            step=1,
            precision=0
        )
    
    btn = gr.Button("Télécharger", variant="primary")
    output = gr.File(label="Fichier ZIP résultant")
    
    examples = gr.Examples(
        examples=[[
            "https://www.radiofrance.fr/franceculture/podcasts/serie-la-nuit-du-merveilleux-scientifique",
            11
        ]],
        inputs=[url_input, num_input]
    )

    btn.click(
        fn=download_podcast,
        inputs=[url_input, num_input],
        outputs=output,
        api_name="download"
    )

app.launch()