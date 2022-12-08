"""
Exercice : 24 to 12
(slide 14)

Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.


Exemples d’utilisation :
$> ruby exo.rb 23:40
11:40PM

Attention : midi et minuit.

"""
#Fonction Conversion heure au format 24h en heure au format 12h
def Format12h(h,m):
    if h > 12 and h < 24:
        h = h - 12
        print(str(h) + ":" + str(m) + " PM")
    elif h < 12 and h > 0:
        print(str(h) + ":" + str(m) + " AM")
    elif h == 12:
        x = int(input("Taper 1 pour : Midi Taper 0 pour : Minuit "))
        if x == 1:
            print(str(h) + ":" + str(m) + " AM")
        elif x == 0:
            print("00" + ":" + str(m))
        else:
            print("Erreur, vous n'avez tapé ni 1, ni 0")
    
#Récupération de l'heure tapée par l'utilisateur & conversion en entier
print("Taper l'heure au format HH:MM")
x = input()
#Stockage de l'heure dans un tableau deux colonnes
heure = x.split(":")
#Envoi des de l'heure et des minutes tapé par l'utilisateur à la fonction Format12h
print(Format12h(int(heure[0]), int(heure[1])))

