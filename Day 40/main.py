#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from sheety import sheety
from datetime import *

data = DataManager()
sheet_data = data.get_data()
fs = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        if row['iataCode'] == '':
            row['iataCode'] = fs.get_code(row['city'])
            data.update_data(row['iataCode'],row['id'])

ORIGIN_CITY_IATA = "LON"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = fs.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue
    if flight.price < destination["lowestPrice"]:

        users = data.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        notification_manager.send_sms(message)
        notification_manager.send_emails(emails, message)

# print("Welcome to Harsh's Flight Club.\n \
# We find the best flight deals and email them to you.")

# first_name = input("What is your first name? ").title()
# last_name = input("What is your last name? ").title()

# email1 = "email1"
# email2 = "email2"
# while email1 != email2:
#     email1 = input("What is your email? ")
#     if email1.lower() == "quit" \
#             or email1.lower() == "exit":
#         exit()
#     email2 = input("Please verify your email : ")
#     if email2.lower() == "quit" \
#             or email2.lower() == "exit":
#         exit()

# print("OK. You're in the club!")

# sheety.add_row(first_name, last_name, email1)