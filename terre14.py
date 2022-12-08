"""
Exercice : Trié ou pas
(slide 17)

Créez un programme qui détermine si une liste d’entiers est triée ou pas.

Exemples d’utilisation :
$> ruby exo.rb 9 8 3
Pas triée !

$> ruby exo.rb 3 8 9 12
Triée !

$> ruby exo.rb “Salut”
erreur.

"""
t = []
def verifTriage(t):
    i = 0

    for nombre in t:
        if t[i] == str:
            print("Erreur")
            exit()
        i = i + 1

    j = 0  
    while j < len(t)-1:
        resultat = int(t[j]) - int(t[j+1])
        
        if resultat > 0:
            print("Pas triée !")
            exit()
        j = j + 1

    print("Triée !")

#Récupération des entiers tapés par l'utilisateur
x = input("Taper des nombres entiers ")

#Rangement des entiers dans un tableau en les splitant par le caractère espace
tableau = x.split(" ")

try:

    i = 0  
    while i < len(tableau):
        tableau[i] = int(float(tableau[i]))
        i = i + 1

    print(verifTriage(tableau))

except ValueError:
    print("Erreur, la valeur entree est une chaine")
    exit()
