import tkinter as tk
import threading
from tkinter import ttk


class BlackjackBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Bot")

        # Variables pour la configuration du bot
        self.mise_de_base = tk.StringVar()
        self.multiplicateur = tk.StringVar()
        self.limite_croupier = tk.StringVar(value="16")
        self.limite_solde = tk.StringVar()

        # Variables pour les statistiques
        self.nombre_parties = tk.StringVar()
        self.mise_actuelle = tk.StringVar()
        self.gain_perte = tk.StringVar()

        # Champs de saisie et sélecteurs pour la configuration du bot
        self.make_entry("Mise de base :", self.mise_de_base)
        self.make_entry("Multiplicateur en cas de défaite :", self.multiplicateur)
        self.make_selector("Limite de pioche : croupier", ["16", "17"], self.limite_croupier)
        self.make_entry("Arrêt automatique à partir de :", self.limite_solde)

        # Frame pour les boutons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        # Bouton pour calibrer le bot
        self.calibrate_button = tk.Button(button_frame, text="Calibrer", command=self.calibrate_bot)
        self.calibrate_button.pack(side=tk.LEFT)

        # Bouton pour démarrer/arrêter le bot
        self.bot_on = False
        self.bot_button = tk.Button(button_frame, text="Démarrer", command=self.toggle_bot)
        self.bot_button.pack(side=tk.LEFT)

        # Labels pour les statistiques
        self.make_label("Nombre de parties :", self.nombre_parties)
        self.make_label("Mise actuelle :", self.mise_actuelle)
        self.make_label("Gain/Perte :", self.gain_perte)

        # Bot
        self.bot = BlackjackBot(self)
        self.bot_thread = None

    # Créer un champ de saisie avec un label
    def make_entry(self, text, var):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame, textvariable=var)
        entry.pack(side=tk.LEFT)
        frame.pack()

    # Créer un sélecteur avec un label
    def make_selector(self, text, options, var):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)
        selector = ttk.Combobox(frame, values=options, textvariable=var, state="readonly")
        selector.pack(side=tk.LEFT)
        frame.pack()

    # Créer un label avec une variable
    def make_label(self, text, var):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)
        value_label = tk.Label(frame, textvariable=var)
        value_label.pack(side=tk.LEFT)
        frame.pack()

    # Fonction pour calibrer le bot
    def calibrate_bot(self):
        self.bot.calibrate()

    # Démarrer ou arrêter le bot
    def toggle_bot(self):
        self.bot_on = not self.bot_on
        if self.bot_on:
            self.bot_button.config(text="Arrêter")
            # Démarrer le bot dans un nouveau thread
            self.bot_thread = threading.Thread(target=self.bot.start)
            self.bot_thread.start()
        else:
            self.bot_button.config(text="Démarrer")
            # Interrompre le bot
            self.bot.stop()

    # Fonction pour exécuter le bot
    def run_bot(self):
        # Ici, vous pouvez mettre le code pour exécuter le bot
        # N'oubliez pas de vérifier régulièrement self.bot_on pour savoir si le bot doit s'arrêter
        # Et mettez à jour les statistiques avec les nouvelles valeurs
        while self.bot_on:
            # Mettez ici le code pour une partie de Blackjack
            # Par exemple :
            # jouer_partie()
            # self.nombre_parties.set(int(self.nombre_parties.get()) + 1)
            pass

    # Fonction pour arrêter le bot
    def stop_bot(self):
        # Ici, vous pouvez mettre le code pour arrêter le bot
        # Par exemple, vous pourriez utiliser une variable de condition pour signaler au bot qu'il doit s'arrêter
        pass

# Créer l'application
root = tk.Tk()
app = BlackjackBotApp(root)
root.mainloop()
