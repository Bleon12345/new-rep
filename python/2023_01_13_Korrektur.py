#Aufgabe 1
def negativ(zahl):
    if zahl < 0:
        print("Negativ")
    else:
        print("nicht Negativ")

#Aufgabe 2
def kleinste(zahl1, zahl2, zahl3):
    if zahl1 < zahl2 and zahl1 < zahl3:
        print(zahl1)
    if zahl2 < zahl1 and zahl2 < zahl3:
        print(zahl2)
    if zahl3 < zahl1 and zahl3 < zahl2:
        print(zahl3)
    else:
        print(zahl3)

#Aufgabe 3

def summe_oder_produkt(zahl1, zahl2):
    if zahl1 + zahl1 < zahl2 * zahl2:
        print(zahl1 + zahl2)
    else:
        print(zahl1 * zahl2)

