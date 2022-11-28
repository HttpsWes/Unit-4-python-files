from turtle import *
from random import randint, choice as rand_choice

colors = ['blue', 'red', 'green', 'grey', 'purple','brown', 'orange']

speed(0)

for i in range (75):
    penup()
    setposition(randint(-200,200), randint(-200,200))
    pendown()

    begin_fill()
     # color(rand_choice(colors))
    pencolor(rand_choice(colors))
    fillcolor(rand_choice(colors))
    pensize(3)
    circle(randint(10,50), steps=randint(4,10))
    right(randint(0,180))
    end_fill()

    


done()