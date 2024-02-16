import requests
from datetime import datetime

GENDER = 'male'
WEIGHT = 58
HEIGHT_CM = 172
AGE = 25

APP_ID = "look from notes"
API_KEY = "look from notes"

today  = datetime.now()
date = f"{today.strftime('%d')}/{today.strftime('%m')}/{today.strftime('%Y')}"
exercise = input("Tell me what exercise you did? ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/8c2af2956e1d17d8486c69674b250f60/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key":API_KEY
}

parameters = {
    "query":exercise,
    "gender":GENDER,
    "weight_kg" : WEIGHT,
    "height_cm":HEIGHT_CM,
    "age":AGE
}
response = requests.post(exercise_endpoint,headers=headers,json=parameters)
result = response.json()
print(result)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
        "date":date,
        "time":today.strftime('%X'),
        "exercise":exercise["name"].title(),
        "duration":exercise["duration_min"],
        "calories":exercise["nf_calories"]
}
    }
    bearer_headers = {
    "Authorization": "look from the notes"
    }
    sheet_response = requests.post(sheety_endpoint,json=sheet_inputs)
    print(sheet_response.text)