###########################
# Auteur: Pierre Coucheney 
###########################

#######################
# import des librairies

import tkinter as tk
import random as rd


############################
# Définition des constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# taille de la grille
N = 4

# choix des couleurs
COUL_MUR = "grey"
COUL_VIDE = "white"

# paramètres de l'automate
# probabilité d'avoir un mur à l'initialisation
P = 0.5


######################
# variables globales

terrain = []
grille = []

#######################
# fonctions

def init_terrain():
    """ Initilise le terrain de la manière suivante:
    * met à 0 la liste à 2D appelée terrain qui contient pour chaque case la 
    valeur 1 si il y a un mur, et 0 sinon
    * initialise la liste à 2D grille qui contient l'identifiant
    de chaque carré dessiné sur le canevas 
    """
    global grille, terrain
    # on réinitialise les variables et le canvas
    grille = []
    terrain = []
    canvas.delete()
    for i in range(N):
        terrain.append([0]*N)
        grille.append([0]*N)

    for i in range(N):
        for j in range(N):
            if rd.uniform(0, 1) < P:
                terrain[i][j] = 1
                couleur = COUL_MUR
            else:
                couleur = COUL_VIDE
            largeur = LARGEUR // N
            hauteur = HAUTEUR // N
            x0, y0 = i * largeur, j * hauteur
            x1, y1 = (i + 1) * largeur, (j + 1) * hauteur
            rectangle = canvas.create_rectangle((x0, y0), (x1, y1), fill=couleur)
            grille[i][j] = rectangle


def affiche_terrain():
    """ Affiche le terrain sur le canvas"""
    for i in range(N):
        for j in range(N):
            if terrain[i][j] == 0:
                coul = COUL_VIDE
            else:
                coul = COUL_MUR
            canvas.itemconfigure(grille[i][j], fill=coul)


def sauvegarde():
    """ Ecrit la valeur N et la variable terrain
        dans le fichier sauvegarde.txt
    """
    fic = open("sauvegarde.txt", "w")
    fic.write(str(N) + "\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(terrain[i][j]) + "\n")
    fic.close()    



def load():
    """Lit le fichier sauvegarde.txt et met à jour les variables
     N et terrain en conséquence, et modifie l'affichage
    """
    global N
    fic = open("sauvegarde.txt", "r")
    ligne = fic.readline()
    N = int(ligne)
    init_terrain()
    i = j = 0
    for ligne in fic:
        n = int(ligne)
        terrain[i][j] = n
        j += 1
        if j == N:
            j = 0
            i += 1
    fic.close()
    affiche_terrain()



#######################
# programme principal

# définition des widgets
racine = tk.Tk()
racine.title("Génération de terrain")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="blue")
bouton_sauv = tk.Button(racine, text="Sauvegarde", command=sauvegarde)
bouton_load = tk.Button(racine, text="Charger terrain", command=load)

# placement des widgets
canvas.grid(column=1, row=0, rowspan=10)
bouton_sauv.grid(row=0)
bouton_load.grid(row=1)


init_terrain()

# boucle principale
racine.mainloop()