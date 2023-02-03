
import random

ja_nein = input("Willst du Schere Stein Papier mit mir spielen??")

if ja_nein == "ja":
    x = random.randint(1,3)
    y = input("Nimmst du Schere Stein oder Papier? ")
    if x == 1 and y == "Schere":
        print("Unentschieden")
    if x == 1 and y == "Stein":
        print("D\ ei /n")
        print("Ge\gn/er")
        print(" ni\/mmt")
        print("SCH/\ERE")
        print(" ()  ()")
        print("Du hast gewonnen")
    if x == 1 and y == "Papier":
        print("     ___________")
        print("    / Dein     /")
        print("   / Gegner   / ")
        print("  /  nimmt   /  ")
        print(" /  PAPIER  /   ")
        print("/__________/    ")
        print("Du hast verloren.Versuche es nocheinmal")
    if x == 2 and y == "Stein":
        print("  ****")
        print("**Dein****")
        print("** Gegner*****")
        print("*** nimmt****")
        print("  **STEIN**")
        print("   *****")
        print("Unentschieden")
    if x == 2 and y == "Papier":
        print("Du hast gewonnen")
    if x == 2 and y == "Schere":
        print("Du hast verloren.Versuche es nocheinmal")
    if x == 3 and y == "Papier":
        print("Unentschieden")
    if x == 3 and y == "Schere":
        print("Du hast gewonnen")
    if x == 3 and y == "Stein":
        print("Du hast verloren.Versuche es nocheinmal")



"""
     ___________
    / Dein     /
   / Gegner   /
  /  nimmt   /
 /  PAPIER  /
/__________/


Zwei Pakete: script (rgbkrk)
platformio-ide-terminal (platformio)

D\ ei /n
Ge\gn/er
 ni\/mmt
SCH/\ERE
 ()  ()



   ****
 **Dein****
** Gegner*****
*** nimmt****
  **STEIN**
   *****
"""
