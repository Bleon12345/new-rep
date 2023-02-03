# Aufgabe 1: Erstelle eine Variable s1, die den String "Katze" enthält.
s1 = "katze"

# Aufgabe 2: Gib den Inhalt der Variable s1 aus.
print(s1)

# Aufgabe 3: Erstelle eine Variable s2, die den String "abc123?" enthält.
s2 = "abc123?"

# Aufgabe 4: Gib den Inhalt der Variable s2 aus.
print(s2)

# Aufgabe 5: Erstelle eine variable s3, die s1 verknüpft/konkateniert mit s2 enthält.
s3 = s1 + s2

# Aufgabe 6: Gib den Inhalt der Variable s3 aus.
print(s3)

# Aufgabe 7: Erstelle eine Variable i1, die den Integer 10 enthält.
i1 = 10

# Aufgabe 8: Gib den Inhalt der Variable i1 aus.
print (i1)
    
# Aufgabe 9: Erstelle eine Variable i2, die das 5-fache von i1 enthält.
i2 = i1 * 5

# Aufgabe 10: Gib den Inhalt der Variable i2 aus.
print(i2)

# Aufgabe 11: Erstelle eine Variable i3, die die Summe aus i1 und i2 enthält.
i3 = i1 + i2 

# Aufgabe 12: Gib den Inhalt der Variable i3 aus.
print(i3)

# Aufgabe 13: Erzeuge eine zufällige Zahl zwischen 1 und 10 und speichere diese in einer Variable i4.
import random
i4 = random.randint(1,10)

# Aufgabe 14: Gib den Inhalt der Variable i4 aus.
print(i4)

# Aufgabe 15: Falls die Zahl in i4 gleich 10 ist, gib "10!" aus.
if i4 == 10:
    print("10!")

# Aufgabe 16: Falls die Zahl in i4 größer als 5 ist, gib "Größer 5!" aus.
if i4 > 5:
    print("Größer 5!")

# Aufgabe 17: Falls die Zahl in i4 größer oder gleich 5 ist, gib "Größer-gleich 5!" aus.
if i4 >= 5:
    print("Größer-gleich 5!")

# Aufgabe 18: Falls die Zahl in i4 kleiner 4 ist, gib "Kleiner 4!" aus.
if i4 < 4:
    print("Kleiner 4!")

# Aufgabe 19: Falls die Zahl in i4 gleich 1 ist, gib "1!" aus, in allen anderen Fällen "Ungleich 1!".
if i4 == 1:
    print("1!") 
else:
    print("Ungleich 1!")


# Aufgabe 20: Falls die Zahl in i4 gleich 1 ist, gib "1!" aus, ansonsten falls die Zahl noch kleiner als 6 ist,
# gib "Zwischen 2 und 5!" aus, in allen anderen Fällen "Größer 5!".
if i4 == 1:
    print("1!"")

elif i4 < 6:
    print ("Zwischen 2 und 5")
else:
    print("Größer 5!")
# Aufgabe 21: Falls die Zahl in i4 gleich 1 ist, gib "1!" aus, ansonsten falls die Zahl noch kleiner als 6 ist,
# gib "Zwischen 2 und 5!" aus, ansonsten, falls die Zahl noch kleiner als 10 ist, gib "Zwischen 6 und 9!" aus,
# in allen anderen Fällen "10!".
if i4 == 1:
    print("1!")
elif i4 < 6:
    print("Zwischen 2 und 5")
elif i4 < 10:
    print("zwischen 6 und 9")
else:
    print("10!")