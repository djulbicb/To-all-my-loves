# API - Application Programming Interface
# Api je interfejs, barijere izmedju tvog i externog sistema.
# Sitem salje request i dobija response data. Request prati pravila

# Primeri api: coinbase, nba leagues, yahoo weather
# Kao u restoranu, ima meni i govori sta mozes da porucis a sta ne. To je api, meni.

# Api endpoint - je lokacija podataka na ekstersnom servisu
# http://api.open-notify.org/iss-now.json
# Plugin: Json Viewer awesome

# Responses
# https://httpstatuses.com/
# 1xx - hold on
# 2xx - success, here is data
# 3xx - dont have permission
# 4xx - client screwed up
# 5xx - server screwed up

import requests
from datetime import datetime
import time
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response, response.status_code, response.json())

# umesto rucno pisanje exceptiona
if response.status_code != 200:
    print("There was an error")
    # raise Exception("Bad error")
response.raise_for_status()

# Json
def is_iss_overhead():
    MY_LAT = 44.869389
    MY_LONG = 20.640221
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    iss_position = (latitude, longitude)
    print(iss_position)

    # My position +-5
    if MY_LAT - 5 <= iss_position[0] <= MY_LAT + 5 and MY_LONG - 5 <= iss_position[1] <= MY_LONG + 5:
        return True
    else:
        return False


# Api sunset
# https://www.latlong.net/
# https://api.sunrise-sunset.org
def is_night():
    MY_LAT = 44.869389
    MY_LONG = 20.640221
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    # response = requests.get(f"https://api.sunrise-sunset.org/json?lat={iss_position[0]}&lng={iss_position[1]}&date=today")
    response = requests.get("https://api.sunrise-sunset.org/json", params)
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.now().hour
    if (current_hour >= sunset_hour and current_hour <= sunrise_hour):
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("Send email")