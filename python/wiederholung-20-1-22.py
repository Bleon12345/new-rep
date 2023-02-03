
# Datentypen
# eine Variable mitt dem Datentyp String (Wörter / Text) kreieren

from concurrent.futures.process import _threads_wakeups


x = "abc"

Frage = "Was für ein tag benutz ..."

# eine Variable mit dem Datentyp Integer (ganze Zahlen) kreieren

x = 123
ergebnis_der_Rechnung = 13

# eine Variable mit dem Datentyp Float (Zahlen mit Nachkommastellen) kreieren

x = 1.23
der_wert_der_aktie = 1.23

# eine Variable mit dem Datentyp Boolean(True oder False) kreieren
wahrheit_gesagt = True

positive_meinung = True
negative_meinung = False

# while Schleifen
# Alle Zahlen zwischen 3 und 340 ausdrucken

zähler=3
ende=340
while zähler<=ende:
    print(zähler)
    zähler = zähler+1

print("_______________________")

# Alle Zahlen zwischen -30 und 8000 (10er Schritte) ausdrucken

zähler=-30
ende=8000 
while zähler<=ende:
    print(zähler)
    zähler = zähler+10

print("_______________________")

# Alle Zahlen zwischen -160 und 75 inklusie  (5er Schritte) ausdrucken

zähler=-160
ende=75
while zähler<=ende:
    print(zähler)
    zähler = zähler+5

# for Schleifen
# Alle Zahlen zwischen 3 und 340 ausdrucken

print("_______________________")

for i in range(3, 341):
    print(i)

# Alle Zahlen zwischen -30 und 8000 (10er Schritte) ausdrucken

print("_______________________")
for i in range(-30,8001, 10):
    print(i)

# Alle Zahlen zwischen -160 und 75 inklusie  (5er Schritte) ausdrucken

for i in range(-160, 76, 5):
    print(i)

#Listen
# eine neue Liste imt mindestens 4 Elementen kreieren

umsatz_liste = [4078.87, 1234.09, 7378.55, 3343.23]
print(umsatz_liste)

# das erste Element auf True setzen

umsatz_liste[0] = True
print(umsatz_liste)

# das vierte Element auf False setzen

umsatz_liste[3] = False
print(umsatz_liste)

# das dritte Element auf "Hello World" setzen

umsatz_liste[2] = ("Hello World")
print(umsatz_liste)

# das erste Element aus der Liste entfernen

umsatz_liste.remove(True)

# ein neues Element am Ende hinzufügen

umsatz_liste.append(1)

# eine Liste mit 2000 mal die 2 kreieren

liste = [2] * 2000

#List Comprehensions
# eine Liste mit allen Zahlen zwicschen -5 und 35 inklusive kreieren

liste = [i for i in range (-5, 36)]
print(liste)