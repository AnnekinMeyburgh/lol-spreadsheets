import os

def get_sheet(service, spreadsheet_id, sheet, range):
    range_name = f"{sheet}!{range}"

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, 
        range=range_name
    ).execute()

    rows = result.get('values', [])

    return rows

def get_lol_sheet(service, sheet, range):
    spreadsheet_id = os.environ['LOL_SPREADSHEET_ID']
    return get_sheet(service, spreadsheet_id, sheet, range)

def get_lol_sheets_info(service):
    spreadsheet_id = os.environ['LOL_SPREADSHEET_ID']
    response = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    return response.get('sheets',[])

def get_lol_sheet_info(service, sheet_name):
    for sheet in get_lol_sheets_info(service):
        if sheet['properties']['title'] == sheet_name:
            return sheet

def get_lol_sheet_names(service):
    sheets = get_lol_sheets_info(service)
    return {sheet['properties']['title'] for sheet in sheets}