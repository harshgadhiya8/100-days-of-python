import os
os.system('cls')
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
count=0
data=[]
def bidder_data(name,bid):
    temp_dict = {
        "Name": name,
        "Bid Amount" : bid
    }
    data.append(temp_dict)
while count!=1:
    print("welcome to the secret auction program")
    name = input("what is your Name?: ")
    bid = int(input("What is your bid?: "))
    bidder_data(name,bid)
    choice = input("Is there any other bidder? ").lower()
    if choice == "yes":
       os.system('cls')
    else:
       count +=1
       os.system('cls')

print(data)
# data2=[{'Name': 'harsh', 'Bid Amount': 78}, 
#        {'Name': 'asd', 'Bid Amount': 78},
#         {'Name': 'sdafds', 'Bid Amount': 675868},
#         {'Name': 'fdhg', 'Bid Amount': 90}, 
#        {'Name': 'uilrwhgr', 'Bid Amount': 7834}, 
#        {'Name': 'blue', 'Bid Amount': 894},
#         {'Name': 'maaaaaa', 'Bid Amount': 67}, 
#        {'Name': 'dhdegfwl', 'Bid Amount': 47}]
count=len(data)
max_value = data[len(data)-1]["Bid Amount"]
print(max_value)
while count>0:
    if data[count-2]["Bid Amount"]>max_value:
        max_value=data[count-2]["Bid Amount"]
        j=count-2
    count-=1
print(f"{data[j]['Name']} wins the bid with {data[j]['Bid Amount']}")

