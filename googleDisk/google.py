import os
import io
import asyncio
import httplib2
import apiclient.discovery
import config
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build


CREDENTIALS_FILE = config.CREDETIALS_FILE

async def down_drive(text, data):
    spreadsheet_id = config.SHEETS_TASKO
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    list = [[text], [data]]

    resource = {
        "majorDimension": "COLUMNS",
        "values": list
    }
    range = "Плановые работы!A:B"
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        body=resource,
        valueInputOption="USER_ENTERED"
    ).execute()
