"""
Exercice : Inverser une chaîne
(slide 9)

Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.


Exemples d’utilisation :
$> node exo.js “Hello world!”
!dlrow olleH


$> node exo.js “lehciM”
Michel

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

"""

#Fonction
def inverseChaine(chaine):
    tableau = []

    for lettre in chaine:
        tableau.append(lettre)

    tailleDeLaChaine = len(tableau)

    #Boucle pour afficher la chaîne inversée
    while tailleDeLaChaine > 0:
        print(end=tableau[tailleDeLaChaine-1])
        tailleDeLaChaine = tailleDeLaChaine - 1 

#Parsing
entreeClavier = input("Taper une phrase à inverser \n")

#Affichage
inverseChaine(entreeClavier)

