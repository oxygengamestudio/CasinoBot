from tkinter import Tk, Label, Button, messagebox
import pyautogui
import json
import os

class BlackjackBot:
    def __init__(self, app):
        self.app = app
        self.mise_de_base = None
        self.multiplicateur = None
        self.limite_croupier = None
        self.limite_solde = None
        self.config_file = "bot_config.json"
        self.coordinates = {}

        # Charger les coordonnées sauvegardées, si elles existent
        try:
            with open(self.config_file, 'r') as f:
                self.coordinates = json.load(f)
        except FileNotFoundError:
            pass

    def calibrate(self):
        print("Calibrating bot...")

        elements_to_calibrate = ['jetons_1', 'jetons_2', 'jetons_5', 'jetons_25', 'jetons_50', 'jetons_100',
                                 'jeu_de_carte', 'cartes_croupier', 'cartes_joueur', 'popup_decision', 'resultat']

        root = Tk()
        root.attributes('-alpha', 0.3)  # Make the window transparent
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")  # Make the window fullscreen
        root.configure(bg="black")  # Set the background color to black

        # Ajout d'un label pour indiquer l'élément à calibrer
        instruction_label = Label(root, text="Cliquez sur l'élément à l'écran", font=("Arial", 24), fg="white", bg="black")
        instruction_label.pack(pady=50)

        for element in elements_to_calibrate:
            print(f"Cliquez sur {element} à l'écran")
            instruction_label.config(text=f"Cliquez sur {element.replace('_', ' ')} à l'écran")

            clicked = False
            coordinates = []

            def on_click(event):
                nonlocal clicked
                nonlocal coordinates
                clicked = True
                coordinates = [event.x, event.y]

            root.bind("<Button-1>", on_click)  # Bind the left click to the on_click function

            while not clicked:
                root.update()

            self.coordinates[element] = coordinates
            print(f"Enregistré les coordonnées pour {element} : {coordinates}")

        instruction_label.destroy()
        root.destroy()

        # Sauvegarder les coordonnées pour une utilisation ultérieure
        with open(self.config_file, 'w') as f:
            json.dump(self.coordinates, f)

        print("Calibration terminée.")

    def start(self):
        # Vérifier si le fichier de calibration existe
        if not os.path.exists(self.config_file):
            messagebox.showerror("Erreur", "Le fichier de calibration est manquant. Veuillez d'abord calibrer le bot.")
            return

        # Récupérer les informations de configuration
        self.mise_de_base = self.app.mise_de_base.get()
        self.multiplicateur = self.app.multiplicateur.get()
        self.limite_croupier = self.app.limite_croupier.get()
        self.limite_solde = self.app.limite_solde.get()

        # Afficher les informations de configuration dans la console
        print(f"Mise de base : {self.mise_de_base}")
        print(f"Multiplicateur en cas de défaite : {self.multiplicateur}")
        print(f"Limite de pioche : croupier : {self.limite_croupier}")
        print(f"Arrêt automatique à partir de : {self.limite_solde}")
        # Ici, vous pouvez mettre le code pour démarrer le bot
        # Par exemple, cela pourrait impliquer de jouer une partie de Blackjack
        print("Starting bot...")

        while self.app.bot_on:
            # Mettez ici le code pour une partie de Blackjack
            # Par exemple :
            # - Détecter les clics sur les jetons
            # - Détecter les clics sur les boutons
            # - Prendre des décisions en fonction des clics détectés
            pass

    def stop(self):
        # Insérez ici le code pour arrêter le bot
        # Par exemple, cela pourrait impliquer de terminer le jeu en cours
        print("Stopping bot...")

    def play_blackjack(self):
        # Insérez ici le code pour jouer une partie de blackjack
        # En utilisant les coordonnées enregistrées pour interagir avec l'interface du jeu
        pass

