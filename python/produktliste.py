produktliste = [5, 10, 12, 2, 99, 14.99, 19.99, 8,88]

summe = 0
for element in produktliste:
    summe = summe + element
print(summe)

print("Durchschnitt = ", summe/len(produktliste))

def max_wert_liste(liste):
    max_wert = liste[0]
    index = 0
    while index <= len(liste) - 1:
        if max_wert < liste[index]:
            max_wert=liste[index]
        index=index+1

    print(max_wert)
max_wert_liste(produktliste)




def min_wert_liste(liste):
    min_wert = liste[0]
    index = 0
    while index <= len(liste) - 1:
        if min_wert > liste[index]:
            min_wert = liste[index]
        index=index + 1

    print(min_wert)
min_wert_liste(produktliste)




"""for i in range(-3000,6001):
    print(i)
print("Please Wait")
print(" Please Wait")
print("  Please Wait")
print("   Please Wait")
print("    Please Wait")
print("     Please Wait")
print("    Please Wait")
print("   Please Wait")
print("  Please Wait")
print(" Please Wait")
print("Please Wait")
print(" Please Wait")
print("  Please Wait")
print("Thanks for Waiting!")

for i in range(-100,276,5):
    print(i)"""
