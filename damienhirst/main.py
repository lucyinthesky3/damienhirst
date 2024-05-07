# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#print(rgb_colors)

import turtle as t
from turtle import Screen
import random

color_list = [(247, 252, 250), (185, 225, 87), (130, 145, 207), (246, 246, 250), (202, 121, 151), (132, 234, 158), (210, 67, 183), (128, 70, 207), (157, 81, 38), (122, 150, 67), (59, 82, 149), (127, 206, 165), (178, 190, 214), (63, 21, 69), (166, 62, 154), (76, 135, 94), (211, 167, 126), (20, 54, 180), (223, 170, 202), (156, 237, 16), (17, 61, 97), (102, 148, 117), (169, 113, 102)]

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(135)
tim.forward(300)
tim.setheading(0)

def draw(space, x):
    for i in range(x):
        for j in range(x):
            tim.dot(20, (random.choice(color_list)))
            tim.forward(space)
        tim.backward(space * x)
        tim.right(90)
        tim.forward(space)
        tim.left(90)

tim.penup()
draw(50, 10)






screen = Screen()
screen.exitonclick()