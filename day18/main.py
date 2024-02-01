from turtle import Turtle,Screen
import random
import os
os.system('cls')
lad = Turtle()
directions = [0,90,180,270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
lad.speed('fastest')
def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        lad.color(random.choice(colours))
        lad.circle(100)
        lad.setheading(lad.heading()+gap_size)
draw_spirograph(5)
# lad.pensize(5)

# for _ in range(200):
#     lad.color(random.choice(colours))
#     lad.forward(30)
#     lad.setheading(random.choice(directions))

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         lad.forward(100)
#         lad.right(angle)

# for shape_side_n in  range(3,11):
#     draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()