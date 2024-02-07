from turtle import Turtle,Screen
import random
class Food(Turtle):
     def __init__(self):
          super().__init__()
          self.shape('circle')
          self.penup()
          self.shapesize(0.5,0.5)
          self.color('blue')
          self.speed('fastest')
          random_x = random.randint(-180,180)
          random_y = random.randint(-230,230)
          self.goto(random_x,random_y)
     def refresh(self):
          random_x = random.randint(-180,180)
          random_y = random.randint(-230,230)
          self.goto(random_x,random_y)
