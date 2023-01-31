import turtle
from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()
screen.listen()
timmy.setheading(90)



def move_forwards():
    timmy.forward(15)

def move_backwards():
    timmy.backward(15)

def move_left():
    timmy.left(15)
    move_forwards()

def move_right():
    timmy.right(15)
    move_forwards()

def back_home():
    timmy.home()

def jump():
    timmy.penup()
    move_forwards()
    timmy.pendown()

def back_home():
    timmy.penup()
    timmy.home()
    timmy.pendown()
    timmy.setheading(90)

def clear():
    timmy.clear()
    back_home()
    timmy.setheading(90)


screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=jump, key="space")
screen.onkey(fun=back_home, key="q")
screen.onkey(fun=clear, key="c")
