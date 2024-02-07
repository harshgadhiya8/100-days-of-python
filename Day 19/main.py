from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
is_race_on =  False
user_bet = screen.textinput(title = 'Make your bet', prompt = 'Which won will win the race? Enter the color: ')
colors = ['red','green','purple','orange','blue','yellow']
y_pos = [-70,-40,-10,20,50,80]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>215:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
    

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()

# screen.listen()
# screen.onkey(key='w',fun=move_forward)
# screen.onkey(key='s',fun=move_backward)
# screen.onkey(key='a',fun=turn_left)
# screen.onkey(key='d',fun=turn_right)
# screen.onkey(key = 'c', fun = clear)
screen.exitonclick()