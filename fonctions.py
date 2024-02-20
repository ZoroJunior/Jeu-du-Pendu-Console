"""
Ici residerons toutes les fonctions qui décriront les différentes actions réalisées dans le programme :
- La gestion des scores sur la fin du jeu
- L'appel, la nomination, la salutaion des joueurs
- L'entree des lettres et la gestion du nombre coup du mot actuel et du nombre de coup restant
- Les messages de victoire et de defaite

"""
import random

import donnees

def gest_Scores(nomFichier,nomDuJOueur,score) :
    with open(nomFichier,"a") as fic :
        fic.write("Joueur {:<5} {:<10} score : {:<3}\n".format(fic.tell()//36, nomDuJOueur, score))

def hello() :
    name = input("Quel est votre nom ou pseudo M./Mme ... ")
    print("Bonjour monsieur {:^10} Nous sommes content de vous voir \nCommencons donc <^-^>".format(name))
    return name

def gest_Avancement(liste) :
    if liste[1] == "" :
        liste[1] = donnees.ListeDesMots["mot{}".format(random.randint(1,10))]
        liste[0] = ["*"]*len(liste[1])

    lettre = input("entrer une lettre svp ")
    if lettre.lower() in liste[1].lower():
        print(donnees.messageLettreTrouve)
        for i in range(len(liste[1])) :
            if liste[1][i].lower() == lettre.lower() :
                liste[0][i] = liste[1][i]
        print("Le mot actuel est : {:>10}".format("".join(liste[0])))
    else:
        print(donnees.messageLettreErrone)
        print("Le mot actuel est : {:>10}".format("".join(liste[0])))

    liste[-1] += -1
    print("Il vous reste {:>3} coup(s) à jouer \n".format(liste[-1]))

    if liste[1].lower() == "".join(liste[0]).lower() :
        print(donnees.messageMotTrouve)
        return 100
    elif liste[-1] == 0 :
        print(donnees.messageMotErrone)
        return liste[0].count("*")*100/len(liste[0])
    else:
        gest_Avancement(liste)

"""

liste[0] = mot caché
liste[1] = mot à trouver
liste[2] = nombre de coup 

"""