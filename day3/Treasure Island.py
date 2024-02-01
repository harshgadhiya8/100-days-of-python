print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
side_choice = input("You want to go Left or Right? ")
side_choice = side_choice.lower()
if side_choice == "left":
    swim_choice = input("Do you want to swim or wait? ")
    swim_choice = swim_choice.lower()
    if swim_choice == "wait":
        color_choice = input("Chose a color between Red, blue and yellow. ")
        color_choice = color_choice.lower()
        if color_choice == "yellow":
            print("You Win")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")