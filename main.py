import turtle as turtle_module
import random

turtle_module.colormode(255)
van = turtle_module.Turtle()
x = 30
color_list = [(43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56)]
van.penup()
van.speed('fastest')

def create_dot(turtle):
    for i in range(10):
        van.dot(x, random.choice(color_list))
        van.penup()
        van.fd(65)

def new_position(x_pos, y_pos):
    van.setposition(x_pos, y_pos)
    create_dot(van)

new_position(-300, -300)
new_position(-300, -240)
new_position(-300, -180)
new_position(-300, -120)
new_position(-300, -60)
new_position(-300, 0)
new_position(-300, 60)
new_position(-300, 120)
new_position(-300, 180)
new_position(-300, 240)
new_position(-300, 300)




screen = Screen()
screen.exitonclick()
