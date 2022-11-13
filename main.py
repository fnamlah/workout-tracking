import requests
import os
from datetime import datetime
APP_ID = os.environ.get("ID")
API_KEY = os.environ.get("KEY")
USERNAME = os.environ.get("NAME")
PASSCODE = os.environ.get("CODE")
LINK = os.environ.get("LINK")
exercise_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell which exercise you did today?: ")
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 173.64,
    "age": 27
}

response = requests.post(url=exercise_Endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result["exercises"][0]["nf_calories"])
print(result["exercises"][0]["name"])


sheety_endpoint = f"https://api.sheety.co/{LINK}/workoutTracking/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    add_row = requests.post(url=sheety_endpoint, json=body, auth=(USERNAME, PASSCODE))
    add_row.raise_for_status()
    result_2 = add_row.json()
    print(result_2)

"""
echo "# workout-tracking" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git push -u origin main
"""
