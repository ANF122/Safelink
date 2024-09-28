import requests
import customtkinter as ctk
from tkinter import messagebox

# Initialisation de CustomTkinter
ctk.set_appearance_mode("dark")  # Thème par défaut
ctk.set_default_color_theme("blue")  # Couleur par défaut

# Fonctions existantes

def check_website(api_key, url):
    api_url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {
        'apikey': api_key,
        'resource': url,
        'allinfo': 'false'
    }
    response = requests.get(api_url, params=params)
    
    try:
        return response.json()
    except ValueError:
        messagebox.showerror("Erreur", "La réponse du serveur n'est pas valide.")
        return {}

def evaluate_site(result):
    if 'positives' in result:
        positives = result['positives']
        total = result['total']
        if positives > 0:
            return f"Site faible (Détéctions: {positives}/{total})"
        else:
            return "Site fiable (Pas de détections)"
    else:
        return "Aucune information disponible pour ce site"

def on_check_button_click():
    api_key = entry_api_key.get().strip()
    if not api_key:
        messagebox.showerror("Erreur", "Veuillez saisir votre clé API.")
        return

    urls = entry_urls.get("1.0", "end").strip().splitlines()
    results = []

    for url in urls:
        if url.strip():
            result = check_website(api_key, url.strip())
            evaluation = evaluate_site(result)
            results.append(f"{url.strip()}: {evaluation}")

    messagebox.showinfo("Résultats", "\n".join(results))

# Fonction pour changer le thème
def change_theme(theme):
    if theme == "Anarchiste":
        root.configure(fg_color="#FF0000")
        label_api_key.configure(fg_color="#FF0000", text_color="#000000")
        label_urls.configure(fg_color="#FF0000", text_color="#000000")
        entry_urls.configure(fg_color="#000000", text_color="#FF0000")
        check_button.configure(fg_color="#000000", text_color="#FF0000")
    elif theme == "Communiste":
        root.configure(fg_color="#FF0000")
        label_api_key.configure(text_color="#FFFF00")
        label_urls.configure(text_color="#FFFF00")
        entry_urls.configure(fg_color="#000000", text_color="#FF0000")
        check_button.configure(fg_color="#FFFF00", text_color="#000000")
    elif theme == "Manga":
        root.configure(fg_color="#e6f7ff")  # Bleu clair
        label_api_key.configure(text_color="#ff66b2")  # Rose
        label_urls.configure(text_color="#ff66b2")
        entry_urls.configure(fg_color="#ffffff", text_color="#000000")
        check_button.configure(fg_color="#ffcc00", text_color="#000000")  # Jaune
    elif theme == "VirusTotal":
        root.configure(fg_color="#2b2d42")  # Bleu nuit
        label_api_key.configure(text_color="#ffffff")
        label_urls.configure(text_color="#ffffff")
        entry_urls.configure(fg_color="#3a3f47", text_color="#ffffff")
        check_button.configure(fg_color="#007bff", text_color="#ffffff")  # Bleu
    elif theme == "Cyberpunk":
        root.configure(fg_color="#00ffcc")  # Vert fluo
        label_api_key.configure(text_color="#000000")
        label_urls.configure(text_color="#000000")
        entry_urls.configure(fg_color="#000000", text_color="#00ffcc")  # Inversé vert fluo
        check_button.configure(fg_color="#ff00ff", text_color="#000000")  # Rose fluo
    elif theme == "Dark Mode":
        root.configure(fg_color="#1e1e1e")  # Gris foncé
        label_api_key.configure(text_color="#ffffff")
        label_urls.configure(text_color="#ffffff")
        entry_urls.configure(fg_color="#2d2d2d", text_color="#ffffff")
        check_button.configure(fg_color="#007acc", text_color="#ffffff")  # Bleu foncé
    elif theme == "Call of Duty":
        root.configure(fg_color="#3a3a3a")  # Gris foncé
        label_api_key.configure(text_color="#00ff00")  # Vert militaire
        label_urls.configure(text_color="#00ff00")
        entry_urls.configure(fg_color="#000000", text_color="#ffffff")
        check_button.configure(fg_color="#00ff00", text_color="#000000")  # Vert militaire
    elif theme == "Battlefield":
        root.configure(fg_color="#1c1c1c")  # Noir
        label_api_key.configure(text_color="#ffcc00")  # Jaune
        label_urls.configure(text_color="#ffcc00")
        entry_urls.configure(fg_color="#000000", text_color="#ffcc00")
        check_button.configure(fg_color="#ffcc00", text_color="#000000")

# Configuration de la fenêtre principale
root = ctk.CTk()
root.title("Safelink")



# Menu de sélection de thème
theme_label = ctk.CTkLabel(root, text="Choisir un thème :")
theme_label.pack(pady=10)

theme_options = ["Anarchiste", "Communiste", "Manga", "VirusTotal", "Cyberpunk", "Dark Mode", "Call of Duty", "Battlefield"]
theme_combo = ctk.CTkComboBox(root, values=theme_options, command=change_theme)
theme_combo.pack(pady=5)
theme_combo.set("Anarchiste")  # Thème par défaut

# Champs de saisie pour la clé API
label_api_key = ctk.CTkLabel(root, text="Clé API :")
label_api_key.pack(pady=10)
entry_api_key = ctk.CTkEntry(root, width=300, show='*')
entry_api_key.pack(pady=5)

# Champ de saisie pour les URLs
label_urls = ctk.CTkLabel(root, text="URLs à vérifier (une par ligne) :")
label_urls.pack(pady=10)
entry_urls = ctk.CTkTextbox(root, height=200, width=300)
entry_urls.pack(pady=5)

# Bouton pour lancer la vérification
check_button = ctk.CTkButton(root, text="Vérifier", command=on_check_button_click)
check_button.pack(pady=20)

# Lancement de la boucle principale de l'interface
root.mainloop()
