print("Hallo,was möchtest du umwandeln?")
print("Meter in Millimeter?")
print("oder")
print("Milliliter in Liter")
print("oder")
print("Millimeter in Kilometer")

x=input()



if "Meter in Millimeter" == x:

    print("Wieviel Meter möchtest du in Millimeter umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    print(x*1000)




if "Milliliter in Liter" == x:

    print("Wieviel Milliliter möchtest du in Liter umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    print(x*0.001)




if "Millimeter in Kilometer" == x:

    print("Wieviel Millimeter möchtest du in Kilometer umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    print(x*0.000001)
