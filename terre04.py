"""
Exercice : Pair ou impair
(slide 7)

Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..


Exemples d’utilisation :
$> ruby exo.rb 2
pair

$> ruby exo.rb 5
impair


$> ruby exo.rb Bonjour
Tu ne me la mettras pas à l’envers.

$> ruby exo.rb
Tu ne me la mettras pas à l’envers.

Attention : gérez aussi les entiers négatifs.

"""
#Fonction
def pairOuImpair(a):
    resultat = entreeClavier % 2

    if resultat == 0:
        print("Pair")
    else:
        print("Impair")

try:
    #Parsing
    print("Choisir un nombre")
    entreeClavier = int(input())

    #Affichage
    pairOuImpair(entreeClavier)

#Gestion d'erreur
except ValueError:
    print("Erreur, la valeur doit être un entier")
    exit()
