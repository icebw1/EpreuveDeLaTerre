"""
Exercice : 12 to 24
(slide 15)

Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.


Exemples d’utilisation :
$> ruby exo.rb 11:40PM
23:40

Attention : midi et minuit.


"""
#Fonction 
def Format24h(h,m):
    if h > 0 and h < 12:
        h = h + 12
        print(str(h) + ":" + str(m))
    elif h > 12 and h < 24:
        print(str(h) + ":" + str(m))
    elif h == 12:
        x = int(input("Taper 1 pour : Midi Taper 0 pour : Minuit "))
        if x == 1:
            print(str(h) + ":" + str(m) + " AM")
        elif x == 0:
            print("00" + ":" + str(m))
        else:
            print("Erreur, vous n'avez tapé ni 1, ni 0")

try:
    #Parsing
    print("Taper l'heure au format HH:MM PM")
    x = input()
    heure = x.split(" ")
    heure.remove("PM")
    heure1 = heure[0].split(":")

    #Affichage
    print(Format24h(int(heure1[0]), int(heure1[1])))

#Gestion d'erreur
except ValueError:
    print("Erreur, vous devez taper l'heure au format indiqué")
    exit()
