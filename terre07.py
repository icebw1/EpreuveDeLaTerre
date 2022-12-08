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
#Récupération de l'entrée tapée par l'utilisateur 
entreeClavier = input()

#Tableau dans lequel sera stocké l'entrée
tableau = []

#Remplissage du tableau
for lettre in entreeClavier:
    tableau.append(lettre)

#Verification que l'entrée ne contient pas d'espace
for lettre in tableau:
    if lettre == " ":
        print("Erreur")
        exit()

i = 0
#La boucle tourne tant que le tableau contient des valeurs
while tableau:
    tableau.pop(-1) #La fonction pop permet de supprimer des valeurs, ici 1 seule
    i = i + 1       #On compte le nombre de fois qu'un caractère a été supprimé

print(i)

