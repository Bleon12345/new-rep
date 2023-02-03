



















"""
1 euro entspricht 1.21 us-dollar
"""

print("Was willst du umwandeln?")
print("euro in dollar")
print("dollar in euro")
print("euro in pfund ")
print("pfund in euro")
print("euro in yen")
print("yen in euro")
print("yen in euro formatiert")
print("bitcoin in euro")
print("bitcoin in euro formatiert")
x=input()
if "dollar in euro" == x:

    print("Wieviel dollar möchtest du in euro umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    print(x*0.83)
if "euro in dollar" == x :

    print("Wieviel Euro möchtest du in Dollar umwandeln")

    x=input()
    x=float(x)
    print("okay,hier:")
    print(x*1.21)

if "pfund in euro" == x:

    print("Wieviel pfund möchtest du in euro umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    print(x*1.16)

if "euro in pfund" == x:

    print("Wieviel euro möchtest du in pfund umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    print(x*0.86)

if "euro in yen" == x:

    print("Wieviel euro möchtest du in yen umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    print(x*132.82)


if "yen in euro" == x:

    print("Wieviel yen möchtest du in Euro umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    print(x*0.0075)


if "yen in euro formatiert" == x:

    print("Wieviel yen möchtest du in Euro umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    euro=x*0.0075
    euro="{:.2f}".format(euro)
    print(euro)

if "bitcoin in euro" == x:

    print("Wieviel bitcoin möchtest du in euro umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    euro=x*29908.78
    print(euro)


if "bitcoin in euro formatiert" == x:

    print("Wieviel bitcoin möchtest du in euro umwandeln")
    x=input()
    x=float(x)

    print("okay,hier:")
    euro=x*29908.78
    euro="{:.2f}".format(euro)
    print(euro, "€")


