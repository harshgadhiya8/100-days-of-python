import random
a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
rock ='''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
'''

paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
'''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
'''
if a>3 or a<0:
    list = [rock,paper,scissors]
    b =random.randint(0,2)
    print(b)

    print(f"You chose {list[a]}")
    print(f"Computer chose {list[b]}")
    if a==0:
        if b==0:
            print("Draw")
        elif b==1:
            print("You won")
        else:
            print("You Lose")
    elif a==1:
        if b==0:
            print("You won")
        elif b==1:
            print("Draw")
        else:
            print("You Lose")
    else:
        if b==0:
            print("You Lose")
        elif b==1:
            print("You won")
        else:
            print("Draw")
else:
    print("invalid choice")



            