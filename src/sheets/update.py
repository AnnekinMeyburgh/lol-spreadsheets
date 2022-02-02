import os
from sheets.get import get_lol_sheet_info

def update_sheet(service, spreadsheet_id, sheet, range, values, value_input_option='RAW', major_dimension='ROWS'):
    range_name = f"{sheet}!{range}"
    body = {
        'majorDimension': major_dimension,
        'values': values
    }
    return service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, 
        range=range_name,
        valueInputOption=value_input_option, 
        body=body
    ).execute()

def update_lol_sheet(service, sheet, range, values, value_input_option='RAW', major_dimension='ROWS'):
    spreadsheet_id = os.environ['LOL_SPREADSHEET_ID']
    return update_sheet(service, spreadsheet_id, sheet, range, values, value_input_option=value_input_option, major_dimension=major_dimension)

def create_lol_sheet(service, sheet_name, from_sheet = None):
    spreadsheet_id = os.environ['LOL_SPREADSHEET_ID']
    if from_sheet is None:
        body = {
            'requests': [
                {
                    'addSheet': {
                        'properties': {
                            'title': sheet_name
                        }
                    }
                }
            ]
        }
    else:
        base_sheet = get_lol_sheet_info(service, from_sheet)
        new_sheet_index = base_sheet['properties']['index'] + 1
        copy_from_sheet_id = base_sheet['properties']['sheetId']
        body = {
            'requests': [
                {
                    'duplicateSheet' : {
                        "sourceSheetId": copy_from_sheet_id,
                        "insertSheetIndex": new_sheet_index,
                        "newSheetName": sheet_name
                    }
                }
            ]
        }
    return service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, 
        body=body
    ).execute()

def remove_lol_sheet(service, sheet_name):
    spreadsheet_id = os.environ['LOL_SPREADSHEET_ID']
    sheet = get_lol_sheet_info(service, sheet_name)
    if sheet is not None:
        body = {
            'requests': [
                {
                    'deleteSheet':{
                        'sheetId': sheet['properties']['sheetId']
                    }
                }
            ]
        }
        return service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id, 
            body=body
        ).execute()

