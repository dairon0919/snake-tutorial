"see https://pastebin.com/hnpyWyVz for tutorial"

import turtle
import time
import random
 
delay = 0.1
 
# Score
score = 0
high_score = 0
 
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("gold")
wn.setup(width=600, height=400)
wn.tracer(0) # Turns off the screen updates
 
# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("Purple")
head.penup()
head.goto(0,0)
head.direction = "stop"
 
# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("cyan")
food.penup()
food.goto(0,100)
 
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 14, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
 
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
 
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
 
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")