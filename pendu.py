import donnees
import fonctions

#Enrégistrement du nom et debut du jeu
nomJoueur = fonctions.hello()

#liste de départ
liste = ["","",0,donnees.nombreDeChance]
print(liste)
#Deroulement de la partie
"""
points est une variable qui contiendra plus tard le score du 
joueur actuel sous forme de float
La fonction gest_Avancement gerera le dourelement du jeu cad la reception
des lettres et la mise à jour des mots cachés/a trouver
"""
result = fonctions.gest_Avancement(liste)

"""
Dans cette partie il s'agira d'enregistrer les scores dans un fichier 
On pourra ainsi developper ça plus tard
"""
fonctions.gest_Scores("scores.txt", nomJoueur, liste[2])