bill = 0
height = int(input("What's your height? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age<=18:
        bill = 7
        print("Youth tickets are $7.")
    elif age > 45 and age <55:
        bill=0
        print("Everything is gonna be okay.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your bill is ${bill}.")
else:
    print("Sorry, You can't ride the rollercoaster")



# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
 
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age <= 6:
#         bill = 5
#         print("Young child tickets are $5.")
#     elif age > 6 and age < 13:
#         bill = 7
#         print("Child tickets are $7.")
#     elif age > 14 and age < 20:
#         bill = 12
#         print("Youth tickets are $12.")
#     else:
#         bill = 20
#         print("Adult tickets are $20.")
  
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
  
#     print(f"Your final bill is ${bill}")
 
# else:
#   print("Sorry, you have to grow taller before you can ride.")
    
