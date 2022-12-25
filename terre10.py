"""
Exercice : Nombre premier
(slide 13)

Créez un programme qui affiche si un nombre est premier ou pas.

Exemples d’utilisation :
$> node exo.js 5
Oui, 5 est un nombre premier.

$> node exo.js 6
Non, 6 n’est pas un nombre premier.

Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.
"""
#Fonction
def Premier(a):
    i = 2
    while i < a:
        resultat = a % i
        if resultat == 0:
            print("Non, " + str(a) + " n'est pas un nombre premier.")
            exit()
        
        else:
            print("Oui, " + str(a) + " est un nombre premier.")
            exit()

        i = i + 1

try: 
    #Parsing
    print("Taper la valeur du nombre")
    x = int(input())

    #Gestion d'erreur
    if x < 0:
        print("Erreur, le nombre doit être positif")
        exit()

    elif x == 0:
        print("Erreur, 0 n'est pas un nombre premier")
        exit()

    elif x == 1:
        print("Erreur, 1 n'est pas un nombre premier")
        exit()

    #Affichage
    print(Premier(x))

#Gestion d'erreur
except ValueError:
    print("Erreur, vous devez taper un entier")
    exit()

