
import httplib2
import apiclient.discovery
import config
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = config.CREDETIALS_FILE

async def down_drive(text, data, spreadsheet_id):
    if spreadsheet_id != '':
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

async def main_google(date, data, data1, data2, data3, spreadsheet_id):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    list = [[date], [data], [data1], [data2], [data3]]

    resource = {
        "majorDimension": "COLUMNS",
        "values": list
    }
    range = "Логирование!A:E"
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        body=resource,
        valueInputOption="USER_ENTERED"
    ).execute()