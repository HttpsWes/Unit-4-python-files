from turtle import *

begin_fill()
color("gold")

circle(100)
end_fill()


def eye():
    penup()
    color("white")
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(180)
    pendown()
    begin_fill()
    color("white")
    circle(25)
    end_fill()
    begin_fill()
    circle(10)
    color("black")
    end_fill()

    penup()
    forward(100)
    penup()
    begin_fill()
    color("white")
    circle(25)
    end_fill()
    begin_fill()
    circle(10)
    color("black")
    end_fill()

    penup()
    left(180)
    forward(50)
    left(90)
eye()

#Mouth
forward(75)
left(90)
pendown()
begin_fill()
color("red")
circle(25)
end_fill()


done()

