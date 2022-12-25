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

try:
    #Parsing
    print("Taper le nombre dont vous voulez connaître la racine")
    x = int(input())

    #Gestion d'erreur
    if x < 0:
        print("Erreur, le nombre doit être positif")
        exit()

    #Affichage
    print("Resultat = ", Racine(x))

#Gestion d'erreur
except ValueError:
    print("Erreur")
    exit()
