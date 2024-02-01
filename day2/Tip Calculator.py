print("Welcome to the tip calculator")
bill = float(input("What was the bill? $"))
tip_percent = int(input("What percent tip would you like to give? 10,12 or 15? "))
no_of_people = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round((bill+(bill*tip_percent/100))/7,2)}$")