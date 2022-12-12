from turtle import Turtle, Screen
from random import randint, choice as rand_choice

colors = ['blue', 'red', 'green', 'grey', 'purple','brown', 'orange']


class MyTurtle(Turtle):

    def random_shape_color(self, x, y):
        self.color(rand_choice(colors))
        self.penup()
        self.setposition(randint(-200,200),randint(-200,200))
        self.pendown()
        self.circle(randint(10,50), steps=randint(4,10))
    
    def __init__(self):
        super().__init__()
        self.random_shape_color(0,0)
        self.onclick(self.random_shape_color)


turtle1 = MyTurtle()
turtle2 = MyTurtle()



screen = Screen()

screen.mainloop()