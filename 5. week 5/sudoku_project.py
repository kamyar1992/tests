import turtle


def set_starter():
    turtle_object = turtle.Turtle()
    screen_object = turtle.Screen()
    turtle_object.hideturtle()
    screen_object.setup(550, 550)
    turtle_object.penup()
    turtle_object.goto(-225, 225)
    turtle_object.pendown()
    turtle_object.speed(2)
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
        print(float(turtle_object.position()[0]), turtle_object.position()[1])
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
        print(turtle_object.position()[0]+50, 225)
        turtle_object.goto(turtle_object.position()[0]+50, 225)
        turtle_object.pendown()





screen = set_starter()[1]
draw_horizontal_lines(set_starter()[0])
number = turtle.Turtle()
number.hideturtle()
number.write('1')
screen.exitonclick()


