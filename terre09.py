"""
Exercice : Racine carrée d'un nombre
(slide 12)

Créez un programme qui affiche la racine carrée d’un entier positif.


Exemples d’utilisation :
$> node exo.js 9
3

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.


"""
#Fonction Racine <=> Elever un nombre à l'exposant 1/2
def Racine(a):
    return pow(a, 1/2)

#Récupération de l'entrée tapée par l'utilisateur & conversion en entier
print("Taper la valeur du nombre")
x = int(input())

print("Resultat = ", Racine(x))
