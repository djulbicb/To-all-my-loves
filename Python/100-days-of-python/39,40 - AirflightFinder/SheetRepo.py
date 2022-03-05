import os
from typing import List

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from model.User import *


class SheetRepo:

    def __init__(self, api_key_file: str, spreadsheet_id: str):
        self.api_key_file = api_key_file
        self.spreadsheet_id = spreadsheet_id
        self.credentials = service_account.Credentials.from_service_account_file(
            api_key_file, scopes=[
                'https://www.googleapis.com/auth/spreadsheets']
        )

    def users_read_all(self) -> List[User]:
        users = []
        data = self.read_all(table="Users", end_range="E")[1:]
        for u in data:
            nu = User(name=u[0], surname=u[1], email=u[2], password=u[3], registered=u[4])
            users.append(nu)
        return users

    def read_all(self, table: str, end_range: str, start_range: str = "A1"):
        try:
            service = build('sheets', 'v4', credentials=self.credentials)

            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.spreadsheet_id,
                                        range=f"{table}!{start_range}:{end_range}").execute()
            values = result.get('values', [])

            if not values:
                return []
            else:
                return values

        except HttpError as err:
            print(err)
            return []

    def add(self, data):
        # Example of data
        # data = [["TestName", "TestSurname", "test@gmail.com", dt.datetime.now().strftime("%Y-%m-%d")]]

        service = build('sheets', 'v4', credentials=self.credentials)
        request = service.spreadsheets().values().append(spreadsheetId=self.spreadsheet_id,
                                                         range="Users!A1",
                                                         valueInputOption="USER_ENTERED",
                                                         body={"values": data})
        response = request.execute()
