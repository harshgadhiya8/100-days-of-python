from turtle import Turtle,Screen
ALIGNMENT = 'center'
FONT = ('arial,24,normal')
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('high_score.txt',mode='r') as file:
            file = file.read()
            self.high_score = int(file)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.high_score}',align=ALIGNMENT,font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt',mode='w') as self.a:
                self.a.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
   
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
