"""# Erstelle eine Liste liste1, die alle geraden Zahlen von 0 bis 400 enthält
liste1 = [i for i in range(401) if i % 2 == 0]
liste1 = [i for i in range(0, 401, 2)]
liste1 = [i * 2 for i in range(201)]

# Erstelle eine Liste liste2 aller Quadratzahlen von 0 bis 225 (0 1 4 9 ... 196 225)
liste2 = [i * i for i in range(16)]
liste2 = [i ** 2 for i in range(16)]

# Erstelle eine Liste liste3 aller Zweierpotenzen von 1 bis 1024 (1 2 4 8 ... 512 1024)
liste3 = [2 ** i for i in range(11)]

# TODO Auf 28. Oktober: Alles ab liste4 (außer liste5) gut lernen!

# Erstelle eine Liste liste4 der Zahlen 225 196 169 144 121 100 81 64 49 36 25 16 9 4 1 0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225
liste4 = [i ** 2 for i in range(-15, 16)]

# Erstelle eine Liste liste5 der Zahlen 225 224 221 216 209 200 189 176 161 144 125 104 81 56 29 0
liste5 = [225 - i ** 2 for i in range(16)]

# Erstelle eine Liste liste6, die 100 Zufallszahlen zwischen -250 und 250 enthält
import random
liste6 = [random.randint(-250, 250) for i in range(100)]

# Erstelle eine Liste liste7, die alle positiven Zahlen aus liste6 enthält
liste7 = [i for i in liste6 if i > 0]

# Erstelle eine Liste liste8, die alle Quadrate der Zahlen aus liste6 enthält
liste8 = [i ** 2 for i in liste6]

# Erstelle eine Liste liste9, die 1000 mal die 0 enthält
liste9 = [0 for i in range(1000)]

# Erstelle eine Liste liste10, die 5 mal eine Liste aller Zahlen von 1 bis 5 enthält
liste10 = [[i + 1 for i in range(5)] for j in range(5)]
print(liste10)

# Erstelle eine Liste liste11, die alle Listen [], [1], [1, 2], [1, 2, 3], ..., [1, 2, ..., 99, 100] enthält
liste11 = [[i for i in range(j)] for j in range(101)]
print(liste11)

def listensumme(liste: list) -> int:
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe

# Erstelle eine Liste liste12, die die Summen über alle Listen aus liste11 enthält
# Verwende die Funktion listensumme
liste12 = [listensumme(liste) for liste in liste11]

# Erstelle eine Liste liste13, die alle Zahlen aus liste12 enthält, die durch 3 teilbar sind
liste13 = [i for i in liste12 if i % 3 == 0]

# Erstelle eine Liste liste14, die 10 Listen mit jeweils 10 zufälligen Zahlen zwischen 1 und 10 enthält
# TODO
liste14 = [[random.randint(1,10) for i in range(random.randint(1.10))] for j in range(10)]
# Erstelle eine Liste liste15, die 10 Listen mit jeweils einer zufälligen, zwischen 1 und 10 großen, Anzahl zufälligen an Elementen zwischen 1 und 10 enthält
# TODO
liste15 = [[random.randint(1,10) for i in range(random.randint(1,10))] for j in range(10)]
# Erstelle eine Liste liste16, die eine zufällige, zwischen 1 und 10 große, Anzahl an Listen mit jeweils einer zufälligen, zwischen 1 und 10 großen, Anzahl an zufälligen Element zwischen 1 und 10 enthält
# TODO"""

liste17 = [i for i range (2,1001) if 0 not in i % d for d in range (2 , i)]

liste18 = [i for i in range (0,50)]
print(liste18)

liste19 = [49 - i  for i in range (50)]
print(liste19)