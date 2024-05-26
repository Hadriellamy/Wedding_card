import tkinter as tk
from tkinter import messagebox

def envoyer_carte():
    messagebox.showinfo("Envoi de la carte", "La carte a été envoyée avec succès !")

def creer_carte():
    fenetre = tk.Tk()
    fenetre.title("Carte de mariage Tehila & Hadriel")
    fenetre.geometry("800x700")

    etiquette = tk.Label(fenetre, text="C'est avec une immense joie que nous vous conivions a notre mariage qui aura lieu en eptembre 2024")
    etiquette.pack()

    bouton_envoyer = tk.Button(fenetre, text="Envoyer la carte", command=envoyer_carte)
    bouton_envoyer.pack()

    fenetre.mainloop()

if __name__ == "__main__":
    creer_carte()
