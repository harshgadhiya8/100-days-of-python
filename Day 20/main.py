from turtle import Turtle,Screen
import time
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
xcor = [-10,0,10]
class Snake():
    def __init__(self):
        self.turtles= []
        self.create_snake()
        self.head = self.turtles[0]
    def create_snake(self):
         for _ in range(0,3):
            new_turtle = Turtle('square')
            new_turtle.penup()
            new_turtle.color('white')
            #new_turtle.shapesize(0.5,0.5)
            new_turtle.goto(x=xcor[_],y=0)
            self.turtles.append(new_turtle)
    def move(self):
            for seg in range(len(self.turtles)-1,0,-1):
                new_x = self.turtles[seg - 1].xcor()
                new_y = self.turtles[seg - 1].ycor()
                self.turtles[seg].goto(new_x,new_y)
            self.turtles[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
screen = Screen()
screen.setup(width=400,height=500)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake = Snake()
screen.update()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()






screen.exitonclick()