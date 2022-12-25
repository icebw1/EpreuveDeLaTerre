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
#Fonction
def Division(a, b):
    
    if b != 0:
        resultat = a / b
        reste = a % b
        print("Résultat : " + str(resultat) + " Reste : " + str(reste))

    elif b == 0:
        print("La division par 0 est impossible")


try:
    #Parsing
    print("Choisir un dividende")
    dividende = int(input())

    print("Choisir un diviseur")
    diviseur = int(input())

    #Affichage
    Division(dividende, diviseur)

#Gestion d'erreur
except ValueError:
    print("Erreur, la valeur doit être un entier")
    exit()
