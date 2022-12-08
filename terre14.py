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
    while i < len(t)-1:
        resultat = int(t[i]) - int(t[i+1])

        if resultat > 0:
            print("Pas triée !")
            exit()
        i = i + 1

    print("Triée !")

#Récupération des entiers tapés par l'utilisateur
x = input("Taper des nombres entiers ")

#Rangement des entiers dans un tableau en les splitant par le caractère espace
tableau = x.split(" ")

print(verifTriage(tableau))

"""
        if resultat != int:
            print("Erreur")
            exit()
"""