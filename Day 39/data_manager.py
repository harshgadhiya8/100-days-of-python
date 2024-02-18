import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/Copy from notes/flightDeals/prices"
        self.response = requests.get(self.sheety_endpoint)
        self.data = self.response.json()

    def get_data(self):
        self.response = requests.get(self.sheety_endpoint)
        self.data = self.response.json()['prices']
        return self.data
    
    def update_data(self,iataCode,id):
        self.sheety_update_endpoint = f"https://api.sheety.co/Copy from notes/flightDeals/prices/{id}"
        self.parameters = {
            'price':{
                'iataCode':iataCode                
            }
        }
        self.res = requests.put(self.sheety_update_endpoint,json=self.parameters)


