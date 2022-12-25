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
#Fonction 
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

#Parsing
x = input("Taper des nombres entiers ")
tableau = x.split(" ")

try:

    i = 0  
    while i < len(tableau):
        tableau[i] = int(float(tableau[i]))
        i = i + 1

    #Affichage
    print(verifTriage(tableau))

#Gestion d'erreur
except ValueError:
    print("Erreur, la valeur entree est une chaine")
    exit()
