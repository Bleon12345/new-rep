uhrzeit = float(input("Gib eine beliebige Uhrzeit ein:"))

deci = round((uhrzeit - int(uhrzeit)),2)
if(deci >=0.6 and deci < 1):
    print("Dies ist keine valide Zahl")
else:
    if(uhrzeit > 0 and uhrzeit <= 7):
        print("Bin am schlafen")
    elif(uhrzeit > 7 and uhrzeit <= 8):
        print("Schnell zur Schule")
    elif(uhrzeit > 8 and uhrzeit <= 14):
        print("Bin in der Schule sorry")
    elif(uhrzeit > 14 and uhrzeit <= 14.30):
        print("Essen essen")
    elif(uhrzeit > 14.30 and uhrzeit <= 18):
        print("Ich Spiele Spiele")
    elif(uhrzeit > 18 and uhrzeit <= 18.30):
        print("Mal wieder Essen essen")
    elif(uhrzeit > 18.30 and uhrzeit <= 21):
        print("natürlich am Computer")
    elif(uhrzeit > 21 and uhrzeit <= 23):
        print("Hausaufgaben und Lernen")
    elif(uhrzeit > 23 and uhrzeit <= 24):
        print("Auf den Schlaf vorbereiten")
    
        
