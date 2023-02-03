umsatz_liste = [4078.87, 1234.09, 7378.55, 3343.23, 9862.02, 9999.09, 12873.98, 3026.45, 8327.95, 8359.45, 7465.54, 7348.99]

summe = 0
index = 0
while index <= 1:
    print(umsatz_liste[index])
    index = index + 1

print(umsatz_liste[2]) # drucke das 3te Element aus
print(umsatz_liste[4]) # drucke das 5te Element aus
print(umsatz_liste[5]) # drucke das 6te Element aus

umsatz_liste.append(31)
umsatz_liste.append(39)
umsatz_liste.append(34)

umsatz_liste.remove(4078.87)
umsatz_liste.remove(9999.09)
umsatz_liste.remove(1234.09)
