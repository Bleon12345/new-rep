"""
antwort = input("Wie findest du das Wetter Heute?")
if antwort == "gut!":
    print("ich finds auch gut!")
if antwort == "schlecht!":
     print("ja das stimmt")
"""

















"""
alter = input("Wie alt bist du?")
if alter =="11":
    print("Das ist schön,ich bin 6 Jahre alt!")
if alter =="12":
    print("Das ist schön,ich bin 6 Jahre alt!")
"""


alter = input("Wie alt bist du? ")
print(type(5.8))
try:
    alter_int = int(alter)
    if alter_int < 10 and alter_int > 4:
        print("Du bist also noch in der Grundschule")
    if alter_int > 10 and alter_int < 17:
        print("Du bist schon auf der weiterführenden Schule")
    if alter_int > 148:
        print("Du bist doch schon tot ")
    if alter_int < 1:
        print("Du bist noch nicht geboren")
    if alter_int > 18 and alter_int < 71:
        print("Du bist erwachsen")
    if alter_int > 70 and alter_int< 149:
        print("Du bist so alt wie die Queen")
    if alter_int > 0 and alter_int < 5:
        print("Du bist grade noch in der Vorschule")
except ValueError:
    print("Diese Eingabe kann ich nicht zu einer Zahl umwandeln")
