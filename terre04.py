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
print("Choisir un nombre")

#Récupération du nombre tapé par l'utilisateur & indication à la machine que le nombre est bien un entier
entreeClavier = int(input())

resultat = entreeClavier % 2

if resultat == 0:
    print("Pair")
else:
    print("Impair")
