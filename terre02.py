"""
Exercice : Afficheur d’arguments
(slide 5)

Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.

Exemples d’utilisation :
$> ruby exo.rb je suis solide !
je
suis
solide
!
"""
#Fonction
def ligneParLigne(a):
    for ligne in a:
        print(end=ligne)
        if ligne == " ":
            print(ligne)

#Parsing
entreeClavier = input("Taper une phrase à afficher ligne/ligne \n")

#Affichage
ligneParLigne(entreeClavier)





