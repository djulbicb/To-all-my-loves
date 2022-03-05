# Check weather at 7am, every day
# Array slicing with [start:stop]
# Sending data with twilio

API_KEY: str = "api"
API_URL = "https://api.openweathermap.org/data/2.5/onecall"
lat = 44.787197
long = 20.457273

params = {
    "appid": API_KEY,
    "lat": lat,
    "lon": long,
    "exclude" : "current,minutely,daily"
}

import requests
response = requests.get(API_URL, params=params)
response.raise_for_status()
data = response.json()["hourly"]
print(data, len(data))

# slice = data[start:stop]
data = data[:12]
for hour in data:
    id = int(hour["weather"][0]["id"])
    if id < 700:
        print("Bring an umbrella")

TWILIO_SID = "www"
TWILIO_TOKEN = "www"

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)