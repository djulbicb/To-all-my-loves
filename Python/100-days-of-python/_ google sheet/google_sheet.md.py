# https://www.youtube.com/watch?v=4ssigWmExak
# https://developers.google.com/sheets/api/quickstart/python
#  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# create new project on
# https://console.developers.google.com
# na main view projekta > explore and enable apis > + Enable Api and services button > Add spreadsheet api
# na strani spreadsheet api > Create credentials
#                           > Korak dva je create servis
#                           > Role: Project > Editor
#                           > U Credentials ima email za novi servis account
#                           > Dodaj novi servis account na spreedsheet share
#                           > Na servise accounts, click on account, > Keys > Generate json key

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import datetime as dt

SERVICE_ACCOUNT_FILE = os.environ.get("SERVICE_ACCOUNT_FILE")
SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # Remove .readonly at end of url to writeable

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")
SPREADSHEET_RANGE = 'Users!A1:D'

# https://developers.google.com/sheets/api/quickstart/python
try:
    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE).execute()
    values = result.get('values', [])

    # APPEND
    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append
    # https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{range}:append
    aoa = [["TestName", "TestSurname", "test@gmail.com", dt.datetime.now().strftime("%Y-%m-%d")]]
    request = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID,
                                                     range="Users!A1",
                                                     valueInputOption="USER_ENTERED",
                                                     body={"values": aoa})
    response = request.execute()

    if not values:
        print('No data found.')
    print('Name, Major:')
    for row in values:
        print(row)
except HttpError as err:
    print(err)
