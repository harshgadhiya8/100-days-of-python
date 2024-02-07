import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = {
    "value": 0,
}

def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money['value']}")

def resource_check(ch):
    for _ in MENU[ch]['ingredients']:
        if resources[_] < MENU[ch]['ingredients'][_]:
            print(f"Sorry there is not enough {_}")
            return False
        else: return True

def resource_deduct(ch):
    for _ in MENU[ch]['ingredients']:
        resources[_] = resources[_] - MENU[ch]['ingredients'][_]

def customer_amount():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickels? "))
    pennies =  int(input("How many pennies? "))
    return ((0.25*quarters) + (0.10*dimes) + (0.05*nickles) + (0.01*pennies))

def bill_check(ch):
    paid_amount = customer_amount()
    if paid_amount < MENU[ch]['cost']:
      print("Sorry that's not enough money. Money refunded")
      return False
    elif paid_amount > MENU[ch]['cost']:
      print(f"Here is ${round((paid_amount - MENU[ch]['cost']),2)} in change.")
      money['value'] += MENU[ch]['cost']
      return True
    else:
      money['value'] += MENU[ch]['cost']
      return True

def coffee_machine():
    want_to_continue =  True
    count = 0
    while want_to_continue:    
        ch = input("What would you like? (espresso,latte,cappuccino): ")
        if ch == 'report':
            report()
        elif ch == 'espresso' or ch == 'latte' or ch =='cappuccino':
            if resource_check(ch) :
                if bill_check(ch):
                    print(f"Here is your {ch} ☕")
                    resource_deduct(ch)
        else:
            if input("You entered wrong choice, If you want to exit then type exit: ") == 'exit':
                want_to_continue = False

coffee_machine()