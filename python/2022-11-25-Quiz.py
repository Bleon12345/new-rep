import time
print("Hallo Spieler!")

punkte = 0

gültige_eingabe = False
while gültige_eingabe == False:

    eingabe = input("Wieviele Einwohner hat Spanien?\na) 58330000\nb) 47330000\nc 57330000\nHier Buchstabe eingeben: ")

    if eingabe == "b" or eingabe == "b)":
        gültige_eingabe = True
        punkte = punkte + 1
        print("Prima, richtig!")

    elif eingabe == "a" or eingabe == "a)" or eingabe == "c" or eingabe == "c)":
        gültige_eingabe = True
        print("Leider falsch, es war b")
    else:
        print("Ungültige Eingabe, bitte gib a oder b oder c ein!")

    eingabe = input("Wieviele Einwohner hat Deutschland?\na) 79440000\nb) 88530000\nc 83130000\nHier Buchstabe eingeben: ")

    if eingabe == "c" or eingabe == "c)":
        gültige_eingabe = True
        punkte = punkte + 1
        print("Prima, richtig!")
    elif eingabe == "b" or eingabe == "b)" or eingabe == "a" or eingabe == "a)":
        gültige_eingabe = True
        print("Leider falsch, es war c")    
        ungültige_eingabe = True
    else:
        print("Probiere Nochmal")
    eingabe = input("Wieviele Einwohner hat Kosovo?\na) 13440000\nb) 1873000\nc 18430000\nHier Buchstabe eingeben: ")

    if eingabe == "b" or eingabe == "b)":
        punkte = punkte + 1
        print("Prima, richtig!")
    else:
        print("Probiere Nochmal")


    print("Zähle deine Punkte und merk sie dir,denn jetzt kommt Runde 2")




    eingabe = input("Was ist 12*10\na) 122\nb) 120\nc 102\nHier Zahl eingeben: ",)
    import time
    zeit = time.time()




    if eingabe == "b" or eingabe == "b)":
        gültige_eingabe = True
        punkte = punkte + 1
        print("Prima, richtig!")
    elif eingabe == "a" or eingabe == "a)" or eingabe == "c" or eingabe == "c)":
        gültige_eingabe = True
        print("Leider falsch, es war b")
    else:
        print("Probiere Nochmal.")
    zeit2 = time.time()
    print(zeit2 - zeit)
    

    eingabe = input("Was ist 25*25\na) 2525\nb) 2500\nc 625\nHier Zahl eingeben: ")
    import time
    zeit = time.time()



    if eingabe == "c" or eingabe == "c)":
        gültige_eingabe = True
        punkte = punkte + 1
        print("Prima, richtig!")
    elif eingabe == "a" or eingabe == "a)" or eingabe == "b" or eingabe == "b)":
        gültige_eingabe = True
        print("Leider falsch, es war c")
    else:
        print("Probiere Nochmal")
    zeit2 = time.time()
    print(zeit2 - zeit)




    eingabe = input( )
    import time
    zeit = time.time()



    if eingabe == "b" or eingabe == "b)":
        gültige_eingabe = True
        punkte = punkte + 1
        print("Prima, richtig!")
    elif eingabe == "a" or eingabe == "a)" or eingabe == "c" or eingabe == "c)":
        gültige_eingabe = True
        print("Leider falsch, es war b")
    else:
        print("Probiere Nochmal.")
    zeit2 = time.time()
    print(zeit2 - zeit)

print("Du hast:" + str(punkte))
print("Wenn du 6 Punkte hast bist du perfekt!")
print("Wenn du 5 Punkte hast bist du durchschnittlich.")
print("Wenn du unter 5 hast,ist dein Allgemein Wissen unter dem Durchschnitt.")