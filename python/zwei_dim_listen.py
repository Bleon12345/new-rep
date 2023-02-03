spielbrett=[[0,0,0],
            [0,0,0],
            [0,0,0]]

"""for i in spielbrett:
    print(spielbrett[0])"""

spielbrett[2][1]=1

spielbrett[1][0]=2

spielbrett[0][2]=1

for i in range(0,3):
    print(spielbrett[i])



def eingabe():
    print("Gib die Koordinaten deines Kreises ein.(z.B:2,1)")
    x=input()
    x=float(x)


    i=[x],[x]
    spielbrett=i
2
eingabe()
