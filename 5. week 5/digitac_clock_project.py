# from turtle import *
#
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

import time
import datetime as dt
import turtle

# create a turtle to display time
t = turtle.Turtle()

# create a turtle to create rectangle box
t1 = turtle.Turtle()

# create screen
s = turtle.Screen()

# set background color of the screen
s.bgcolor("green")
s.setup(250, 150)
s.screensize()

# obtain current hour, minute and second
# from the system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
t.hideturtle()
t1.hideturtle()
t1.pensize(3)
t1.color('black')
t1.penup()
t1.speed(1)
# set the position of turtle
TURTLE_SIZE = 40
print(TURTLE_SIZE/2 - s.window_width()/2, s.window_height()/2 - TURTLE_SIZE/2)
t1.goto(TURTLE_SIZE/2 - s.window_width()/2, s.window_height()/2 - TURTLE_SIZE/2)
t.penup()

t.goto(-80, -20)

print(t1.position())
t1.pendown()

# create rectangular box
for i in range(2):
    t1.forward(200)
    t1.right(90)
    t1.forward(70)
    t1.right(90)

# hide the turtle
t1.hideturtle()

while True:
    t.hideturtle()
    t.clear()
    # display the time
    t.write(str(hr).zfill(2)
            + ":" + str(min).zfill(2) + ":"
            + str(sec).zfill(2),
            font=("Arial Narrow", 35, "bold"))
    time.sleep(1)
    sec += 1

    if sec == 60:
        sec = 0
        min += 1

    if min == 60:
        min = 0
        hr += 1

    if hr == 13:
        hr = 1
    # s.exitonclick()

