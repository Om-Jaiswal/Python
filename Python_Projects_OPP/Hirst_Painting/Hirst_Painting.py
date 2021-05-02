#import colorgram
import turtle as turtle_module
import random

#rgb_colors = []
#colors = colorgram.extract('image.jpg',50)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

#print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(227, 230, 236), (243, 236, 242), (244, 239, 226), (235, 243, 239), (194, 166, 108), (135, 167, 193),
              (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10),
              (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104),
              (14, 41, 25), (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217),
              (88, 121, 182), (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15),
              (168, 208, 178), (14, 88, 104), (162, 203, 212), (220, 179, 173), (236, 204, 13)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()