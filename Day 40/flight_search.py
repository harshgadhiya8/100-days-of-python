import requests
from pprint import pprint
from flight_data import FlightData

tequilla_endpoint = "https://api.tequila.kiwi.com"
api_key = 'copy from notes'

class FlightSearch:
    def get_code(self,city_name):
        headers = {
            'apikey':api_key
        }
        query = {
            'term':city_name,
            'location_types':'city'
        }
        response = requests.get(url=f"{tequilla_endpoint}/locations/query",headers=headers,params=query)
        data = response.json()['locations']
        return data[0]['code']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        headers = {
            'apikey':api_key
        }

        response = requests.get(
            url=f"{tequilla_endpoint}/v2/search",
            headers=headers,
            params=query,
        )        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data

