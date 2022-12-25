"""
Exercice : Trouver la Suisse (lol)
(slide 16)

Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.


Exemples d’utilisation :
$> ruby exo.rb 11 40 34
34

$> ruby exo.rb 2 1 3
2

$> ruby exo.rb 2 2 2
erreur.


"""
#Fonction 
def valeurMilieu(a, b, c):
    if c < a < b or b < a < c:
        return a
    elif  c < b < a or a < b < c:
        return b
    elif  a < c < b or b < c < a:
        return c
    elif  a == c == b:
        print("Erreur")

try:
    #Parsing
    x = input("Taper 3 nombres entiers \n")
    tableau = x.split(" ")

    #Gestion d'erreur
    i = 1
    for n in tableau:
        i += 1

        if i != 3:
            print("Erreur, saisissez 3 nombres") 
            exit()


    #Affichage
    print(valeurMilieu(int(tableau[0]), int(tableau[1]), int(tableau[2])))

#Gestion d'erreur
except ValueError:
    print("Erreur, saisissez 3 nombres") 
    exit()

