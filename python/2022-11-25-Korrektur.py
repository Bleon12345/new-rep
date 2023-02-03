# Aufgabe 1
# Erstelle eine Liste liste1, die 10 Listen mit jeweils 10 zufälligen Zahlen zwischen 1 und 10 enthält. Vergiss nicht, benötigte Module zu importieren.
import random
liste1 = [[random.randint(1,10) for i in range(10) for j in range(10)]]

# Aufgabe 2
# Erstelle eine Liste liste2, die alle Primzahlen zwischen 5 und 599 enthält.
liste2 = [i for i in range(5,600) if 0 not in [i % for j in range (2, i)]]