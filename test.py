def ConversionEnInt(t):
    j = 0
    i = 0
    for nombre in tableau:
        if type(nombre) == str:
            while i < len(t):
                t[i] = int(t[i])
                i += 1 
            print("Erreur")
            exit()
        j += 1 

    

    

x = input("Taper des nombres ")

tableau = x.split(" ")

print(tableau)

print(ConversionEnInt(tableau))

if ConversionEnInt:
    print("Ok")
else:
    print("NON OK")

"""
j = 0
for nombre in tableau:
    if type(nombre) == str:
        print("Erreur")
        exit()
    j += 1    

print(tableau) 
"""
