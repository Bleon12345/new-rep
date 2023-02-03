# Schreibe eine Funktion namens hallo, die "unendlich" oft Hallo sagt.
def hallo():
    print("Hallo")
    hallo()



# Schreibe eine Funktion namens hallo_n, die n mal Hallo sagt.
def hallo_n(n):
    if n <= 0:
        return
    print("Hallo")
    hallo_n(n-1)

# Schreibe eine Funktion namens n_bis_eins_ausgabe, die alle Zahlen von n bis 1 ausgibt

def n_bis_eins_ausgabe(n):
    if n <= 0:
        return
    print(n)
    n_bis_eins_ausgabe(n - 1)



# Schreibe eine Funktion namens eins_bis_n_summe, die alle Zahlen von 1 bis n zusammenzählt und zurückgibt
def eins_bis_n_summe(n):
    if n <= 0:
        return 0
    vorgänger = eins_bis_n_summe(n - 1)
    ergebnis = vorgänger + n
    return ergebnis
print(eins_bis_n_summe(10))



def fakultät(n):
    if n <= 0:
        return 1
    vorgänger = fakultät(n - 1)
    ergebnis = vorgänger * n
    return ergebnis

#Schreibe eine Funktion einhundert_n, die einen Parameter n besitzt und n Mal die Zahl 100 ausgibt

def einhundert_n(n):
    if n <= 0:
        return
    print(100)
    einhundert_n(n-1)

#Schreibe eine Funktion eins_bis_n_ausgabe,die einen Parameter n besitzt und alle zahlen von 1 bis n ausgibt(von klein nach groß)

def eins_bis_n_ausgabe(n):
    if n <= 0:
        return
    eins_bis_n_ausgabe(n - 1)

    print(n)



# Schreibe eine Funktion liste_n_mal_eins, die einen Parameter n besitzt und eine Liste zurückgibt, die n Mal die Zahl 1 enethält
liste = [1]
def liste_n_mal_eins(n):
    if n <= 0:
        return
    print(liste)
    liste_n_mal_eins(n - liste)

    liste_n_mal_eins(5)