import os
import json

def get_audio_files():
    # Définir les extensions de fichiers audio à inclure
    audio_extensions = ('.mp3', '.wav')
    # Définir les fichiers à exclure
    excluded_files = {'sounds.json', 'README.md'}
    
    # Obtenir le chemin absolu du répertoire courant
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Liste pour stocker les noms de fichiers
    audio_files = []
    
    # Parcourir tous les fichiers dans le répertoire
    for file in os.listdir(root_dir):
        # Vérifier si le fichier n'est pas dans la liste des exclusions
        # et si son extension correspond à un fichier audio
        if file not in excluded_files and file.lower().endswith(audio_extensions):
            audio_files.append(file)
    
    # Trier la liste alphabétiquement
    audio_files.sort()
    
    return audio_files

def update_json():
    audio_files = get_audio_files()
    
    # Écrire la liste dans le fichier JSON
    with open('sounds.json', 'w', encoding='utf-8') as f:
        json.dump(audio_files, f, indent=4)
    
    print(f"sounds.json mis à jour avec {len(audio_files)} fichiers audio.")

if __name__ == "__main__":
    update_json()