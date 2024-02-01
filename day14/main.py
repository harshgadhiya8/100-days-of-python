from art import logo,vs
from data import data
import os
import random
def choice(a,b):
    print('Who has the higher follower count?')
    print(' A. ' + a['name'] + ', ' + a['description']+ ', from ' +a['country'] )
    print(vs)
    print(' B. ' + b['name']+ ', ' + b['description']+ ', from ' +b['country'])
    return input().lower()
def game(streak):
    print(logo)
    a = random.choice(data)
    b = random.choice(data)
    if a == b:
        b = random.choice(data)
    count = 0
    while count == 0:
        ch = choice(a,b)
        if ch =='a' or ch =='b':
            if ch == 'a':
                pl_choice = a
                com_choice = b
            else:
                pl_choice = b
                com_choice = a
            if pl_choice['follower_count'] > com_choice['follower_count']:
                os.system('cls')
                print('you have guessed it correctly')
                a = pl_choice
                b = random.choice(data)
                if a == b:
                    b = random.choice(data)
                streak+=1
                print(f'Your current streak is {streak}')
            else:
                count+=1
                os.system('cls')
        else:
            print('invalid choice')
            count+=1
    return streak
streak = 0
streak = game(streak)
os.system('cls')
print("Sorry you lose")
print(f"Your streak was {streak}")
