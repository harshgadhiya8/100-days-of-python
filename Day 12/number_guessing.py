import random
import art
import os
os.system('cls')
print(art.logo)
def game(diff_level,number):
    attempts = 0
    count = 0
    if diff_level == 'easy':
      attempts = 10
    elif diff_level == 'hard':
      attempts = 5
    attempt_count = 0
    while count == 0 and attempt_count < attempts:
        guess = int(input(f'You have {attempts - attempt_count} remaining to guess the number '))
        if guess == number:
         print('You have guessed right')
         count = 1
        elif guess < number:
         print('Too low')
         attempt_count +=1
        else:
         print('Too high')
         attempt_count +=1
    if count == 1:
      print(f"You have guessed it correctly, The number was {number} ")
    else:
      print("You have run out of guesses, you lose.")
      print(f"The number was {number}")     
    
print(" Welcome to the number guessing game")
print("I am thinking of a number between 1 to 100")
a = random.randint(1,100)
difficulty_level = input("Chose your difficulty level type 'easy' or 'hard : ").lower()
game(difficulty_level,a)
