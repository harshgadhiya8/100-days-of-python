def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def choice():
    count = 0
    choice = input("Do you want to continue with this calculation? y for yes, r for restart and 0 for exit \n").lower()
    if choice == 'r':
        count+=1
    elif choice == 'y':
        count = 0
    else:
        count = 2 
    return count

operations = {
    '+': add,
    '-': sub,
    "*": mul,
    '/':div
}
def calculator():
    os.system("cls")
    print(art.logo)
    print("Welcome to the calculator")
    c=0
    num1 = int(input("What's the first number\n"))
    num2 = int(input("What's the second number\n"))
    for i in operations:
        print(i)
    op_symbol = input("What operation do you want to do?\n")
    if op_symbol not in operations:
        print("You entered invalid symbol")
    else:
        func =operations[op_symbol]
        answer  = func(num1,num2)
        print(answer)
        c=choice()
        if c == 1:
            calculator()
        elif c == 0:
            while c == 0:
                op_symbol = input("What different operation do you want to do?\n")
                if op_symbol not in operations:
                    c+=1
                    print("You entered invalid symbol")
                else:
                    func =operations[op_symbol]
                    num3 = int(input("Enter another number\n"))
                    answer = func(answer,num3)
                    print(answer)
                    c = choice()
        else:
            os.system("cls")
            print(f"Your final answer is {answer}")
import os
import art
os.system("cls")
print(art.logo)
print("Welcome to the calculator")
c=0
calculator()