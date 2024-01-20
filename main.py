from turtle import Turtle, Screen
from random import randint

tim = Turtle()
purple = Turtle()
blue = Turtle()
red = Turtle()
yellow = Turtle()

tim.penup()
purple.penup()
blue.penup()
red.penup()
yellow.penup()

tim.color("green")
purple.color("purple")
blue.color("blue")
yellow.color("yellow")
red.color("red")

tim.shape('turtle')
purple.shape('turtle')
blue.shape('turtle')
yellow.shape('turtle')
red.shape('turtle')

tim.goto(-240, 150)
purple.goto(-240, 75)
blue.goto(-240, 0)
yellow.goto(-240, -75)
red.goto(-240, -150)

screen = Screen()
screen.setup(width=500, height=400)
user_pick = screen.textinput(title="Make your pick", prompt="Which turtle will win the race? enter a color: ")
print(user_pick)


def random_move(turtle):
    x = randint(1, 10)
    turtle.fd(x)


keep_going = True
while keep_going:
    random_move(tim)
    random_move(purple)
    random_move(blue)
    random_move(yellow)
    random_move(red)

    if tim.xcor() >= 220:
        keep_going = False
        winning_color = "green"
        if winning_color == user_pick:
            print(f"You win! The {winning_color} turtle is the winner!")
        else:
            print(f"You lose. The {winning_color} turtle is the winner!")
    elif purple.xcor() >= 220:
        keep_going = False
        winning_color = "purple"
        if winning_color == user_pick:
            print(f"You win! The {winning_color} turtle is the winner!")
        else:
            print(f"You lose. The {winning_color} turtle is the winner!")
    elif blue.xcor() >= 220:
        keep_going = False
        winning_color = "blue"
        if winning_color == user_pick:
            print(f"You win! The {winning_color} turtle is the winner!")
        else:
            print(f"You lose. The {winning_color} turtle is the winner!")
    elif yellow.xcor() >= 220:
        keep_going = False
        winning_color = "yellow"
        if winning_color == user_pick:
            print(f"You win! The {winning_color} turtle is the winner!")
        else:
            print(f"You lose. The {winning_color} turtle is the winner!")
    elif red.xcor() >= 220:
        keep_going = False
        winning_color = "red"
        if winning_color == user_pick:
            print(f"You win! The {winning_color} turtle is the winner!")
        else:
            print(f"You lose. The {winning_color} turtle is the winner!")














screen.exitonclick()