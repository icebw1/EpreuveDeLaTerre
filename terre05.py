"""
Exercice : Division
(slide 8)

Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.


Exemples d’utilisation :
$> python exo.py 5 2
résultat: 2
reste: 1


$> python exo.py 10 0
erreur.


$> python exo.py 3 5
erreur.

"""
print("Choisir un dividende")
#Récupération du dividende tapé par l'utilisateur & indication à la machine que le nombre est bien un entier
dividende = int(input())

print("Choisir un diviseur")
diviseur = int(input())

while diviseur != 0:
    resultat = dividende / diviseur
    reste = dividende % diviseur
    print("Résultat : " + str(resultat) + " Reste : " + str(reste))

if diviseur == 0:
    print("La division par 0 est impossible")
    
