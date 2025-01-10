# import colorgram
import random
import turtle as t
t.colormode(255)
#
# colors = colorgram.extract('hirst_painting.jpg', 15)
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)
# print(color_list)

colours_in_painting = [(182, 65, 34), (213, 149, 97), (14, 24, 42), (239, 208, 94), (237, 62, 33), (157, 26, 19),
                       (72, 29, 32), (84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37)]


timmy = t.Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()

def turn():
    timmy.left(90)
    timmy.forward(30)
    timmy.left(90)
    timmy.forward(300)
    timmy.right(180)

timmy.setpos(-150.00, -150.00)
for loop in range(10):
    for dot in range(10):
        random_color = random.choice(colours_in_painting)
        timmy.dot(15, random_color)
        timmy.penup()
        timmy.forward(30)
    turn()

















screen = t.Screen()
screen.exitonclick()