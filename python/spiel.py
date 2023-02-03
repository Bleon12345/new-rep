import random
# pip install termcolor
# oder
# pip3 install termcolor
from termcolor import colored

print(colored(" ***********************************", "green","on_red", attrs=["blink"]))
print(colored("Auf welchem Schwierigkeitsgrad möchtest du spielen?","cyan",attrs=["bold", "underline"]))
Schwierigkeitsgrad=input (colored("Leicht, mittel oder schwer? ","green", attrs=["reverse", "bold"]))



geheime_zahl = random.randint(1,100)
if Schwierigkeitsgrad == "Leicht":
    geheime_zahl=random.randint(1,100)
if Schwierigkeitsgrad == "mittel":
    geheime_zahl=random.randint(1,1000)

if Schwierigkeitsgrad == "schwer":
    geheime_zahl=random.randint(1,10000)

for i in range (10,0,-1):
    print()
    print(colored("*************************", "red"))
    print (colored("Du hast noch " + str(i) + " Versuche", "yellow"))
    eingabe1 = input(colored("Bitte gib eine Zahl ein ", "green"))
    eingabe1_als_zahl = int(eingabe1)

    if eingabe1_als_zahl == geheime_zahl:
        print (colored("Du hast die zahl erraten wooow ", "green"))
        break

    if geheime_zahl <eingabe1_als_zahl:
        print(colored("Die Zahl ist **K L E I N E R** als diese Zahl", "blue"))

    if geheime_zahl >eingabe1_als_zahl:
        print(colored("Die Zahl ist **G R Ö ß E R** als diese Zahl", "red"))
