
annee = int(input("Quelle année souhaitez vous analyser?"))
b = "L'année est bissextile"
nb = "L'année n'est pas bissextile"
bissextile = False

if annee % 4 == 0:
    if annee % 400 == 0:
        bissextile = True
    elif annee % 100 == 0:
        bissextile = False
    else:
        bissextile = True
else:
    bissextile = False

if bissextile:
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile")


