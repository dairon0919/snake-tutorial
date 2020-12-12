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
head.shape("square")
head.color("Purple")
head.penup()
head.goto(0,0)
head.direction = "stop"
 
# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)
 
segments = []
wn.mainloop()
