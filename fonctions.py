"""
Ici residerons toutes les fonctions qui décriront les différentes actions réalisées dans le programme :
- La gestion des scores sur la fin du jeu
- L'appel, la nomination, la salutaion des joueurs
- L'entree des lettres et la gestion du nombre coup du mot actuel et du nombre de coup restant
- Les messages de victoire et de defaite

"""

#donnees et random sont des modules python et un de mes modules permettant d'avoir access
# aux fonctions neccesaires tel que randint ainsi qu'aux donnees stockees
import random
import donnees

#Cette fonction prend en entree le nom du fichier ou sera noté les scores le nom du joueur en cours ainsi que son score
def gest_Scores(nomFichier,nomDuJOueur,score) :
    with open(nomFichier,"a") as fic :
        fic.write("Joueur {:<5} {:<10} score : {:<3.2f}\n".format(fic.tell()//36, nomDuJOueur, score))

# fic.tell() donne un retour sur le nombre de caractere deja ecrite car à l'ouverture le curseur
# se trouve en fin de fichier ainsi sachant qu'une ligne fait excatement 36 caractères
# on retrouve facilement le numero de la ligne

#Cette fonction permet permet d'enregistrer le nom du joueur et de lui adresser un message de bienvenu
def hello() :
    name = input("Quel est votre nom ou pseudo M./Mme ... ")
    print("Bonjour monsieur/madame {:^10} Nous sommes content de vous voir \nCommencons donc <^-^>".format(name))
    return name

def gest_Avancement(liste) :
    # """
    #
    # :param liste:
    # :return: score
    # """
    if liste[1] == "" :
        liste[1] = donnees.ListeDesMots["mot{}".format(random.randint(1,10))]
        liste[0] = ["*"]*len(liste[1])
        #
        # Au debut du programme on choisi un mot au hasard dans les mots préremplis
        # puis on cree un mot caché de même taille
        #

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
        liste[2] += -100/donnees.nombreDeChance
        liste[-1] += -1
#
# Dans le bout de code ci dessus on teste l'apparition d'une lettre
# puis on met à jour le mot en cache ainsi que le nombre de coups restants
#
    print("Il vous reste {:>3} coup(s) à jouer \n".format(liste[-1]))

    if liste[1].lower() == "".join(liste[0]).lower() :
        print(donnees.messageMotTrouve)
        return True
    elif liste[-1] == 0 :
        print(donnees.messageMotErrone)
        return False
        # return (liste[0].count("*"))*100/len(liste[0])
    else:
        gest_Avancement(liste)

        # On teste la sortie du programme lorsqu'on obtient le mot
        # ou lorque le nombre de  coups fnit sinon on continue le jeu
        #



# liste[0] = mot caché
# liste[1] = mot à trouver
# liste[2] = nombre de coup
# liste[3] = nombre de coup

