import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]

file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)


#Fetch the sheet
sheet = client.open('Python Sheet').sheet1
python_sheet = sheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(python_sheet)

#Fetch row
row = sheet.row_values(5)
print('\nFetched Row')
pp.pprint(row)

#Fetch column
col = sheet.col_values(2)
print('\nFetched Column')
pp.pprint(col)

#Fetch cell
cell = sheet.cell(3,3)
print('\nFetched Cell')
pp.pprint(cell.value)

#Update Cell
cell = sheet.cell(3,3)
print('Cell Before Update: ',cell.value)
sheet.update_cell(3,3,'N')
cell = sheet.cell(3,3)
print('Cell After Update: ',cell.value)

#Insert Row
row = ['7','https://daily-py.blogspot.com','Y']
index = 8
sheet.insert_row(row,index)