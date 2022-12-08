"""
Exercice : L’alphabet à partir de
(slide 6)

Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.


Exemples d’utilisation :
$> python exo.py n
nopqrstuvwxyz
$>


Attention : votre programme devra utiliser une boucle.

"""
#Déclaration du tableau Alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Récupération de la lettre tapée par l'utilisateur
entreeClavier = input("Choisir une lettre à partir de laquelle afficher l'alphabet \n")

#Initialisation du compteur
i = 0

#Incrémentation du compteur jusqu'à la lettre tapée par l'utilsateur
while entreeClavier != alphabet[i]:
    for lettre in alphabet[i]:
        i += 1

#Affichage de l'alphabet à partir de la lettre tapée par l'utilisateur
while i < 26:
    for lettre in alphabet[i]:
        print(end=lettre)
        i += 1

print("\n")
