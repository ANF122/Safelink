import requests
import tkinter as tk
from tkinter import messagebox, ttk

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

    urls = entry_urls.get("1.0", tk.END).strip().splitlines()
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
        root.configure(bg="#FF0000")
        label_api_key.config(bg="#FF0000", fg="#000000")
        label_urls.config(bg="#FF0000", fg="#000000")
        entry_urls.config(bg="#000000", fg="#FF0000")
        check_button.config(bg="#000000", fg="#FF0000")
    elif theme == "Neutre":
        root.configure(bg="#f0f0f0")
        label_api_key.config(bg="#f0f0f0", fg="#000000")
        label_urls.config(bg="#f0f0f0", fg="#000000")
        entry_urls.config(bg="#ffffff", fg="#000000")
        check_button.config(bg="#007bff", fg="#ffffff")
    elif theme == "Manga":
        root.configure(bg="#e6f7ff")
        label_api_key.config(bg="#e6f7ff", fg="#ff66b2")
        label_urls.config(bg="#e6f7ff", fg="#ff66b2")
        entry_urls.config(bg="#ffffff", fg="#000000")
        check_button.config(bg="#ffcc00", fg="#000000")
    elif theme == "VirusTotal":
        root.configure(bg="#2b2d42")
        label_api_key.config(bg="#2b2d42", fg="#ffffff")
        label_urls.config(bg="#2b2d42", fg="#ffffff")
        entry_urls.config(bg="#3a3f47", fg="#ffffff")
        check_button.config(bg="#007bff", fg="#ffffff")
    elif theme == "Cyberpunk":
        root.configure(bg="#00ffcc")
        label_api_key.config(bg="#00ffcc", fg="#000000")
        label_urls.config(bg="#00ffcc", fg="#000000")
        entry_urls.config(bg="#000000", fg="#00ffcc")
        check_button.config(bg="#ff00ff", fg="#000000")
    elif theme == "Dark Mode":
        root.configure(bg="#1e1e1e")
        label_api_key.config(bg="#1e1e1e", fg="#ffffff")
        label_urls.config(bg="#1e1e1e", fg="#ffffff")
        entry_urls.config(bg="#2d2d2d", fg="#ffffff")
        check_button.config(bg="#007acc", fg="#ffffff")
    elif theme == "Communiste":
        root.configure(bg="#FF0000")
        label_api_key.config(bg="#FF0000", fg="#FFFF00")
        label_urls.config(bg="#FF0000", fg="#FFFF00")
        entry_urls.config(bg="#000000", fg="#FF0000")
        check_button.config(bg="#FFFF00", fg="#000000")
    elif theme == "Call of Duty":
        root.configure(bg="#3a3a3a")  # Gris foncé
        label_api_key.config(bg="#3a3a3a", fg="#00ff00")  # Vert militaire
        label_urls.config(bg="#3a3a3a", fg="#00ff00")
        entry_urls.config(bg="#000000", fg="#ffffff")
        check_button.config(bg="#00ff00", fg="#000000")
    elif theme == "Battlefield":
        root.configure(bg="#1c1c1c")  # Noir
        label_api_key.config(bg="#1c1c1c", fg="#ffcc00")  # Jaune
        label_urls.config(bg="#1c1c1c", fg="#ffcc00")
        entry_urls.config(bg="#000000", fg="#ffcc00")
        check_button.config(bg="#ffcc00", fg="#000000")

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Vérificateur de Site - VirusTotal")

# Remplacer l'icône avec un fichier .ico
root.iconbitmap("logo.ico")  #remplacer par votre chemin relatif 

# Menu de sélection de thème
theme_label = tk.Label(root, text="Choisir un thème :", bg="#282c34", fg="#61afef")
theme_label.pack(pady=10)

theme_options = ["Anarchiste", "Neutre", "Manga", "VirusTotal", "Cyberpunk", "Dark Mode", "Communiste", "Call of Duty", "Battlefield"]
theme_combo = ttk.Combobox(root, values=theme_options)
theme_combo.bind("<<ComboboxSelected>>", lambda event: change_theme(theme_combo.get()))
theme_combo.pack(pady=5)
theme_combo.set("Anarchiste")  # Défaut

# Champs de saisie pour la clé API
label_api_key = tk.Label(root, text="Clé API :", bg="#FF0000", fg="#000000")
label_api_key.pack(pady=10)
entry_api_key = tk.Entry(root, width=50, show='*')
entry_api_key.pack(pady=5)

# Champ de saisie pour les URLs
label_urls = tk.Label(root, text="URLs à vérifier (une par ligne) :", bg="#FF0000", fg="#000000")
label_urls.pack(pady=10)
entry_urls = tk.Text(root, height=10, width=50)
entry_urls.pack(pady=5)

# Bouton pour lancer la vérification
check_button = tk.Button(root, text="Vérifier", command=on_check_button_click)
check_button.pack(pady=20)

# Lancement de la boucle principale de l'interface
root.mainloop()

