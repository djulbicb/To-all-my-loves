import requests

import json
from nutritionix import Nutritionix
import datetime as dt

def pretty_json(json_obj):
    output = json.dumps(json_obj, indent=4, sort_keys=True)
    print(output)

n = Nutritionix()
response = n.process("Ride my bike for 3km")["exercises"][0]
pretty_json(response)


# Sheety
# Morao sam da se izlogujem ulogujem, da bih refreshovao link gmail i aplikacije. Allow edit, delete...
# https://dashboard.sheety.co

headers = {
    "Content-Type": "application/json"
}
url = 'https://api.sheety.co/###/workout/email';
body = {
    "email": {
        "Date" : str(dt.datetime.now().strftime("%Y-%m-%d")),
        "Activity" : response["name"],
        "Calories" : response["nf_calories"]
    }
  }
pretty_json(body)
sheety = requests.post(url=url, json=body, headers=headers)
pretty_json(sheety.json())

# I dont think sheety works anymore. It returns created row index. But table isnt updated