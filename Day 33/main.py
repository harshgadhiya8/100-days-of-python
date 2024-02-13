import requests
from datetime import datetime
MY_LAT = 22.307776
MY_LONG = 70.825278
UTC_HOUR_OFFSET = 5
UTC_MIN_OFFSET = 30
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['longitude']

# print(longitude,latitude)

parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
    "tzid": "Asia/Kolkata"
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

time_now = datetime.now()
print(time_now.hour)
sunrise = data['results']['sunrise'].split("T")[1].split(':')[0]
sunset = data['results']['sunset'].split("T")[1].split(':')[0]

print(sunrise)
print(sunset)

