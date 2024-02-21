# Jeu-du-Pendu-Console

#Voici les règles du jeu et les modalités que j'ai suivi pour aboutir

Votre mission
Nous y voilà. Je vais vous préciser un peu la mission, sans quoi on va avoir du mal à
s'entendre sur la correction.
Un jeu du pendu

Le premier point de la mission est de réaliser un jeu du pendu. Je rappelle brièvement
les règles, au cas où : l'ordinateur choisit un mot au hasard dans une liste, un mot
de huit lettres maximum. Le joueur tente de trouver les lettres composant le mot. À
chaque coup, il saisit une lettre. Si la lettre gure dans le mot, l'ordinateur ache le
mot avec les lettres déjà trouvées. Celles qui ne le sont pas encore sont remplacées par
des étoiles (*). Le joueur a 8 chances. Au delà, il a perdu.

On va compliquer un peu les règles en demandant au joueur de donner son nom, au
début de la partie. Cela permettra au programme d'enregistrer son score.
Le score du joueur sera simple à calculer : on prend le score courant (0 si le joueur
n'a aucun score déjà enregistré) et, à chaque partie, on lui ajoute le nombre de coups
restants comme points de partie. Si, par exemple, il me reste trois coups au moment
où je trouve le mot, je gagne trois points.

Par la suite, vous pourrez vous amuser à faire un décompte plus poussé du score, pour
l'instant cela sura bien.
Le côté technique du problème
Le jeu du pendu en lui-même, vous ne devriez avoir aucun problème à le mettre en
place. Rappelez-vous que le joueur ne doit donner qu'une seule lettre à la fois et que le
programme doit bien vérier que c'est le cas avant de continuer. Nous allons découper
notre programme en trois chiers :
 Le chier donnees.py qui contiendra les variables nécessaires à notre application (la
liste des mots, le nombre de chances autorisées. . .).
 Le chier fonctions.py qui contiendra les fonctions utiles à notre application. Là, je
ne vous fais aucune liste claire, je vous conseille de bien y rééchir, avec une feuille et
un stylo si cela vous aide (Quelles sont les actions de mon programme ? Que puis-je
mettre dans des fonctions ?).
 Enn, notre chier pendu.py qui contiendra notre jeu du pendu.

Gérer les scores
Vous avez, j'espère, une petite idée de comment faire cela. . . mais je vais quand même
clarier : on va enregistrer dans un chier de données, que l'on va appeler scores (sans
aucune extension) les scores du jeu. Ces scores seront sous la forme d'un dictionnaire :
en clés, nous aurons les noms des joueurs et en valeurs les scores, sous la forme d'entiers.
164CORRECTION PROPOSÉE

Il faut gérer les cas suivants :
 Le chier n'existe pas. Là, on crée un dictionnaire vide, aucun score n'a été trouvé.
 Le joueur n'est pas dans le dictionnaire. Dans ce cas, on l'ajoute avec un score de 0 .
À vous de jouer
Vous avez l'essentiel. Peut-être pas tout ce dont vous avez besoin, cela dépend de
comment vous vous organisez, mais le but est aussi de chercher ! Encore une fois, c'est
un exercice pratique, ne sautez pas à la correction tout de suite, cela ne vous apprendra
pas grand chose.
Bonne chance !
