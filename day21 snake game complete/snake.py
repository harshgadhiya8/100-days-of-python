from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
xcor = [(-10,0),(0,0),(10,0)]
class Snake():
    def __init__(self):
        self.turtles= []
        self.create_snake()
        self.head = self.turtles[0]
    
    def create_snake(self):
         for position in xcor:
             self.add_segment(position)
            
    def add_segment(self,position):
        new_turtle = Turtle('square')
        new_turtle.penup()
        new_turtle.color('white')
        #new_turtle.shapesize(0.5,0.5)
        new_turtle.goto(position)
        self.turtles.append(new_turtle)
    
    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend(self):
        self.add_segment(self.turtles[-1].position())

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