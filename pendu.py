import donnees
import random
import fonctions

nomJoueur = fonctions.hello()
liste = ["","",donnees.nombreDeChance]
points = fonctions.gest_Avancement(liste)
fonctions.gest_Scores("scores.txt", nomJoueur, points)