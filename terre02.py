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

entreeClavier = input("Taper une phrase à afficher ligne/ligne")

for ligne in entreeClavier:
    print(end=ligne)
    if ligne == " ":
        print(ligne)
