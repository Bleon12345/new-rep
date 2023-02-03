# Aufgabe 1.1
# Erstelle eine Klasse Prozessor, die vier Attribute Hersteller, Taktfrequenz, Kernzahl und Cache-Speicher besitzt.
# Der Konstruktor der Klasse soll Werte für alle vier Attribute entgegennehmen und diese entsprechend initialisieren.
# Überlege dir passende Datentypen für die Attribute und benenne diese mittels Type-Hints.

class Prozessor:
    def __init__(self, hersteller: str, taktfrequenz: float, kernzahl: int, cache_speicher: str):
        self.hersteller = hersteller
        self.taktfrequenz = taktfrequenz
        self.kernzahl = kernzahl
        self.cache_speicher = cache_speicher

# Aufgabe 1.2
# Erstelle eine Objekt der Klasse Prozessor und speichere dieses in einer Variable p1.Gib als Hersteller AMD, als Taktfrequenz 4.00,
# als Kernzahl 16 sowie als Cache-Speicher 64 MB an.

p1 = Prozessor("AMD", 4.00, 16, "64 MB")


