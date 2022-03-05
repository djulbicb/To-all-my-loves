# https://tequila.kiwi.com/portal/docs/tequila_api
# IATA naples

import os
import json
from SheetRepo import *
from EmailSender import *

SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")
SERVICE_ACCOUNT_FILE = os.environ.get("SERVICE_ACCOUNT_FILE")
KIWI_KEY=os.environ.get("KIWI_KEY")
GMAIL_EMAIL = os.environ.get("GMAIL_EMAIL")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

repo = SheetRepo(api_key_file=SERVICE_ACCOUNT_FILE, spreadsheet_id=SPREADSHEET_ID)
users = repo.users_read_all()
print(users)

sender = EmailSender(email=GMAIL_EMAIL, password=GMAIL_PASSWORD)

import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
headers = {
    "apikey" : KIWI_KEY,
}
params = {
    "fly_from" : "BEG",
    "fly_to" : "NAP",
    "date_from" : dt.datetime.now().strftime("%d/%m/%Y"),
    "date_to" : (dt.datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y"),
    "sort" : "price",
    "limit" : 2
}
data = requests.get("https://tequila-api.kiwi.com/v2/search", params=params, headers=headers)
for offer in data.json()["data"]:
    for user in users:
        print(user.email)
        sender.sendEmail(send_to="djulbic.bojan@gmail.com", message=f"Fly from:{offer['cityFrom']} Fly to: {offer['cityTo']} Price: {offer['price']} Link: {offer['deep_link']}")


