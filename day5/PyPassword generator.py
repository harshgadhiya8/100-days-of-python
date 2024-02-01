import random
alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)] + [chr(i) for i in range(ord('a'), ord('z')+1)]
number = [str(i) for i in range(10)]
symbols = ['!', '@', '#', '$', '%', '&', '*', '+','(',')']
print("Welcome to password generator")
num_alphabets = int(input("How many letters do you want? "))
num_numbers = int(input("How many numbers do you want? "))
num_special = int(input("How many special characters do you want? "))
password = ""
password_list = []
for i in range(1,num_alphabets+1):
    password += alphabet[random.randint(0,len(alphabet)-1)]
    password_list.append(alphabet[random.randint(0,len(alphabet)-1)])
for i in range(1,num_numbers+1):
    password += number[random.randint(0,len(number)-1)]
    password_list.append(number[random.randint(0,len(number)-1)])
for i in range(1,num_special+1):
    password += symbols[random.randint(0,len(symbols)-1)]
    password_list.append(symbols[random.randint(0,len(symbols)-1)])
print(f"Here is your password: {password}")
random.shuffle(password_list)
password2 = ""
for i in password_list:
    password2 += i
print(f"Here is your password: {password2}")