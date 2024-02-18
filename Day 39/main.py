#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
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
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )