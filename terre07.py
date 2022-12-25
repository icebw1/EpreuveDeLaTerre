"""
Exercice : Taille d'une chaîne
(slide 10)

Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.


Exemples d’utilisation :
$> python exo.py “Hello world!”
12


$> python exo.py
erreur.


$> python exo.py “Bonjour” “Aurevoir”
erreur.

$> python exo.py 10
erreur.
"""
#Fonction
def taille(t):
    i = 0
    for i in range(0, len(entreeClavier)):
        tableau.append(entreeClavier[i])
        i+=1

    j = 0
    for lettre in t:
        j+=1

    print(j)


#Parsing    
entreeClavier = input("Taper une phrase pour en obtenir sa taille \n")
tableau = []

#Gestion d'erreur
if entreeClavier.isdigit():
    print("Erreur, l'élément tapé est un entier")
    exit()

#Affichage
taille(entreeClavier)


