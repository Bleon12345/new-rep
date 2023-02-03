"""
liste_von_ints = [1, 2, 3, 4, 5]
print(liste_von_ints)

liste_von_strings = ["Es", "war", "einmal", "vor", "sehr", "langer", "Zeit"]
print(liste_von_strings)

x = 5
y = 8
print(x + y)

x = "Die Hexe "
y = "im Wald"
print(x + y)

# Aufgabe
# Zähle zu jeder Zahl aus der Liste liste_von_ints 2 hinzu
# Am Ende soll liste_von_ints also sein: [3, 4, 5, 6, 7]
for i in range(5):
    liste_von_ints[i] = liste_von_ints[i] * 2
print(liste_von_ints)

for i in [10, 15, 20, 25, 30]:
    print(i)
"""
"""
neue_liste_1 = [7, 4, 13, 19, 14, 1, 5, 11]
#for i in neue_liste_1:
#    if i % 2 == 1:
#        print(i)

neue_liste_2 = [8, 2, 15, 10, 18, 19, 12, 7]
for i in range(len(neue_liste_1)):
    if neue_liste_1[i] > neue_liste_2[i]:
        print(neue_liste_1[i])
    if neue_liste_2[i] > neue_liste_1[i]:
        print(neue_liste_2[i])
"""

neue_liste_1 = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ]
for l in neue_liste_1:
    if l * l  < 70 :
        print(l)
