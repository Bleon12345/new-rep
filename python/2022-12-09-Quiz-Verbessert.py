print("Hallo willkomen zu meinem Quiz und viel Spaß!")

fragenliste = ["Wieviele Einwohner hat Spanien?\na) 58330000\nb) 47330000\nc 57330000\nHier Buchstabe eingeben: ", 
"Wieviele Einwohner hat Deutschland?\na) 79440000\nb) 88530000\nc 83130000\nHier Buchstabe eingeben: ",
"Wieviele Einwohner hat Kosovo?\na) 13440000\nb) 1873000\nc 18430000\nHier Buchstabe eingeben: ",
"Was ist 12*10\na) 122\nb) 120\nc 102\nHier Zahl eingeben: ",
"Was ist 25*25\na) 2525\nb) 2500\nc 625\nHier Zahl eingeben: ",
"Was ist 2*14792\na) 28498\nb) 29584\nc 30024\nHier Zahl eingeben: "]
antwortenliste = ["b", "c", "b", "b"; "c", "b",]
punkteliste = [2, 1, 3, 1, 3, 2]


punkte = 0
i = 0
while i < len(fragenliste):
    gültige_eingabe = False
    while gültige_eingabe == False:
        eingabe = input(fragenliste[i])
        if eingabe == antwortenliste[i] or eingabe == antwortenliste[i] + ")":
            gültige_eingabe = True
            print("Prima, richtig!")
            punkte = punkte + punkteliste[i]
        elif eingabe == "a" or eingabe == "a)" or eingabe == "b" or eingabe == "b)" or eingabe == "c" or eingabe == "c)":
            gültige_eingabe = True
            print("Leider falsch, die richtige Antwort wäre " + antwortenliste[i] + ") gewesen!")
        else:
            print("Ungültige Eingabe,Versuche es erneut")

    i = i + 1

print("So viele Punke hast du erreicht: " + str(punkte))
