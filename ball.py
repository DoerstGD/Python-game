# Python-game
from tkinter import *
from turtle import *


root = Tk()

lbl = Label(root, width=10, height=10, text="AUTO GAME")

lbl.pack()

window = Screen()
window.bgcolor('green')
window.setup(750, 750)
window.title("Мячик")
ball = Turtle('circle')
ball.turtlesize(2)
ball.hideturtle()
ball.color('gold')
ball.penup()

box = Turtle()
box.hideturtle()
box.pensize(20)
box.penup()
box.goto(-200, 200)
box.pendown()
box.color('white')

for side in range(4):
    box.fd(400)
    box.right(90)

ball.goto(100, 100)
dx, dy = 1.3, 2.3
ballX, ballY = 50, 50
ball.speed('fastest')
ball.showturtle()

while True:
    ball.goto(ballX + dx, ballY + dy)
    ballX, ballY = ball.xcor(), ball.ycor()
    if ballX < -168 or ballX > 168:
        dx = dx * -1
    if ballY < -168 or ballY > 168:
        dy = dy * -1
root.mainloop()
