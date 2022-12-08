"""
Exercice : Puissance d'un nombre
(slide 11)

Créez un programme qui affiche le résultat d’une puissance.


L’exposant ne pourra pas être négatif.


Exemples d’utilisation :
$> node exo.js 2 3
8

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

"""

#Fonction Puissance
def Puissance(a, b):
    i = 1
    Resultat = 1
    while i < (b + 1):
        Resultat = Resultat * a
        i = i + 1
    return Resultat

#Récupération de l'entrée tapée par l'utilisateur & conversion en entier

print("Taper la valeur du nombre")
x = int(input())
print("Taper la valeur de son exposant")
y = int(input())

if y < 0:
    print("Erreur, l'exposant ne peut être négatif")
    exit()

print("Resultat = ", Puissance(x, y))
