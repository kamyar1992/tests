import turtle

turtle.tracer()
def set_starter():

    screen_object = turtle.Screen()  # make a screen
    screen_object.setup(550, 550)    # resize the screen

    turtle_object = turtle.Turtle()  # make turtle object
    # turtle_object.hideturtle()       # hide turtle
    turtle_object.penup()
    turtle_object.goto(-225, 225)
    turtle_object.pendown()
    # turtle_object.speed(5)
    turtle_object.pensize(5)

    turtle_object.speed('fastest')
    print(turtle_object.position())
    return turtle_object, screen_object


def draw_horizontal_lines(turtle_object):
    for i in range(10):
        if i == 0 or i == 9:
            turtle_object.pensize(5)
        elif i in (3, 6):
            turtle_object.pensize(3)
        else:
            turtle_object.pensize(1)
        turtle_object.forward(450)
        turtle_object.penup()
        print(turtle_object.position())
        # print(float(turtle_object.position()[0]), turtle_object.position()[1])
        turtle_object.goto(-turtle_object.position()[0], turtle_object.position()[1]-50)
        turtle_object.pendown()
    turtle_object = set_starter()[0]
    turtle_object.right(90)
    for i in range(10):
        if i == 0 or i == 9:
            turtle_object.pensize(5)
        elif i in (3, 6):
            turtle_object.pensize(3)
        else:
            turtle_object.pensize(1)
        turtle_object.forward(450)
        turtle_object.penup()
        # print(turtle_object.position()[0]+50, 225)
        turtle_object.goto(turtle_object.position()[0]+50, 225)
        turtle_object.pendown()


def number_adder(turtle_object):
    # turtle_object.hideturtle()

    turtle_object.pendown()
    print(turtle_object.isvisible())
    turtle_object.forward(100)
    turtle_object.write('1')


draw, screen = set_starter()

draw_horizontal_lines(draw)
# number = turtle.Turtle()
# number.hideturtle()
# number.write('1')
# number_adder(draw)
print(draw.position())
screen.exitonclick()


