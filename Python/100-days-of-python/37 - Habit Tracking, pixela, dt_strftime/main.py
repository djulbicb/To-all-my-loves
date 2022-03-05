import requests
import datetime

PIXELA_URL="https://pixe.la/v1"
PIXELA_TOKEN="###"
PIXELA_USERNAME="###"

# Create user
# =====================================
params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=f"{PIXELA_URL}/users", json=params)
# print(response.json())
# https://pixe.la/@regenbar

# Add graph
# =====================================
PIXELA_GRAPH_URL=f"{PIXELA_URL}/users/{PIXELA_USERNAME}/graphs"
headers={
    "X-USER-TOKEN": PIXELA_TOKEN
}
params={
    "id": "ad4515",
    "name": "test-graph",
    "type": "int",
    "unit": "Joys",
    "color": "ichou"
}
# response = requests.post(url=PIXELA_GRAPH_URL, headers=headers, json=params)
# print(response.text)


# Add point to graph
# =====================================
pixel_creation_endpoint = f"{PIXELA_URL}/users/{PIXELA_USERNAME}/graphs/ad4515"

today = datetime.datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)