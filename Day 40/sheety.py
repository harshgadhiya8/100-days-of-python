import requests
# /8c2af2956e1d17d8486c69674b250f60/flightDeals/users
project = "flightdeals"
sheet = "users"
api = "copy from notes"
base_url = "https://api.sheety.co"

class sheety:
    def __init__(self):
        pass
    def add_row(fname,lname,email):
        sheety_endpoint = f"{base_url}/{api}/{project}/{sheet}"
        headers = {
            "Content-Type": "application/json"
        }
        parameters = {
            "user":{
                'firstName':fname,
                'lastName':lname,
                'email':email
            }
        }
        response = requests.post(url=sheety_endpoint,headers=headers, json=parameters)
        response.raise_for_status()
        print(response.status_code)


