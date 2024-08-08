import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

# ...

def sheets_comparison(last):
    df = pd.ExcelFile(last)
    sheet_names = df.sheet_names
    second = sheet_names[1]
    df = df.parse(second)

    # Create a Google Sheets service
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Get the Google Sheets ID and range
    spreadsheet_id = 'your_spreadsheet_id'
    range_name = 'Sheet1!A1:Z1000'  # adjust the range to your needs

    # Clear the Google Sheets
    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range_=range_name,
        body={}
    ).execute()

    # Copy data from XLSX to Google Sheets
    body = {
        'values': df.values.tolist()
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range_=range_name,
        valueInputOption='USER_ENTERED',
        body=body
    ).execute()

    print('Data copied from XLSX file to Google Sheets')