import requests
from twilio.rest import Client

MY_LAT = 36.892788 # Your latitude
MY_LONG = 30.910662 # Your longitude
end_point="http://api.openweathermap.org/data/2.5/forecast"
api_key = "eef75a8c4f48fcd08de8a66eb5465e11"

account_sid = "stored it in notes"
auth_token = "stored it in notes"

parameters={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid":api_key,
    "cnt": 4
}

response = requests.get(end_point,params=parameters)
data= response.json()
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body="Bring an Umbrella",
        from_= "**********",
        to="***********"
    )
    print(message.status)