import turtle 
import pandas as pd

df = pd.read_csv('50_states.csv')
guessed_state = []

screen = turtle.Screen()
screen.title('US states game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
while len(guessed_state) < 50:
    answer_state = turtle.textinput(title=f'Guessed {len(guessed_state)}/50 states ', prompt="Enter the state's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in df['state'].unique():
            if state not in guessed_state:
                missing_states.append(state)
        new_df = pd.DataFrame(missing_states)
        new_df.to_csv('States to learn.csv')
        break
    if answer_state in df['state'].unique():
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
            x_cor = int(df[df['state']==answer_state].x)
            y_cor = int(df[df['state']==answer_state].y)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x_cor,y_cor)
            t.write(answer_state)
        
        

turtle.mainloop()
