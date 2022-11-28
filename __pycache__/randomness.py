from turtle import *
from random import randint, choice as rand_choice

colors = ['blue', 'red', 'green', 'gery', 'purple','brown', 'orange']

speed(3)

for i in range (75):
    penup()
    setposition(randint(-200,200), randint(-200,200))
    pendown()

    begin_fill()
    color(rand_choice(colors))
    circle(randint(10,50), steps=randint(4,10))
    left,right(0,90)
    end_fill()

    


done()