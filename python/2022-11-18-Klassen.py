class Computer:
    def __init__(self, grafikkarte, prozessor, motherboard, gewicht, uuid, festplattenspeicher, betriebssystem):
        self.grafikkarte = grafikkarte
        self.prozessor = prozessor
        self.gewicht = gewicht
        self.uuid = uuid
        self.motherboard = motherboard
        self.festplattenspeicher = festplattenspeicher
        self.betriebssystem = betriebssystem

computer1 = Computer("Geforce 2080GTX","Intel i9", "ASUS Z2790 LGA", 4.5,"94Rf2000", 512 ,"Windows")
print(computer1.grafikkarte)
computer1.betriebssystem = "Linux"
print(computer1.betriebssystem)

# Eine Klasse Film mit minedestens 5 Attributen von mindestens 4 verschiedenen Datentypen

class Film:
    def __init__(self, drehbuchautor, erscheingungsdatum, genre, dauer, hauptcharakter, jugendfrei):
        self.drehbuchautor = drehbuchautor
        self.erscheingungsdatum = erscheingungsdatum
        self.genre = genre
        self.dauer = dauer
        self.hauptcharakter = hauptcharakter

    def __repr__(self):
        return "Film | Name: " + self.name + "Dauer:" + str(self.dauer) + "Stunden, erscheinungsjahr:" + str(self.erscheinungsjahr)


film = Film("Bleon","01-06-2008", "Action", 128, "Noelb")
print(film.drehbuchautor)
print(film.hauptcharakter)

class Kino:
    def __init__(self, name: str, adresse: str, aktuelle_filme: list):
        self.name = name
        self.adresse = adresse
        self.aktuelle_filme = aktuelle_filme

        def anzahl_filme(self):
            anzahl = len(self.aktuelle_filme)
            return anzahl

        def ins_programm_nehmen(self, film: Film):
            self.aktuelle_filme.append(film)

        def gib_film(self, nummer: int):
            return self.aktuelle_filme[nummer]

        def gib_ersten_film(self):
            return self.aktuelle_filme[0]

        def filme_nach_dauer_sortieren(self):
            pass
        









film1 = Film("Ich einfach unverbesserlich 2", 1.5, "Steve Carell", 2013, ["Kristen Wiig", "Miranda Cosgrove", "Dana Gaier"], True)

film2 = Film("Spiderman", 2.03, "Tom Holland", 2019, ["Jake Gyllenhaal", "Samuel L. Jackson", "Cobie Smulders"], True)

film3 = Film("Andor",9.0,"Ben Caron",2022,["Diego Luna","Adria Arjona",True])


kino1 = Kino("Mathäser", "Bayerstraße 3-5", [film1, film2, film3])
print(kino1.anzahl_filme())

film4 = Film("LYLE: Mein Freund das Krokodil", 1.47,"Shawn Mendes", 2022, ["Constance Wu", "Scoot Mcnairy"], True)

kino1.ins_programm_nehmen(film4)
print(kino1.anzahl_filme())

print(kino1.gib_film(2))