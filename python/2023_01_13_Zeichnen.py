from turtle import *


w = 10000


for i in range(4):
    
    forward(12)
    left(50)
    w = w * 5
right(50)
left(100)
forward(15)

forward(25)
left(90)
forward(7)
for i in range(4):
    
    forward(10)
    left(50)
    w = w * 5
forward(0)

goto(20, -20)

right(110)
forward(35)
right(90)
for i in range(3):
    
    forward(8)
    right(25)
    w = w * 5
right(20)
forward(10)
right(35)
forward(10)
right(30)
forward(20)
right(55)
forward(10)
hideturtle()
done()