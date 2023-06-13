from openpyxl import load_workbook
import re

data_file = '/Users/benbradley/Downloads/Current Time Tracking 🗓️.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file)

# List all the sheets in the file.
sheetNames = ['June-23','Month Nav','Week Template','Dropdown Backend','Ideas...','Jan-23','Feb-23','Mar-23','Apr-23','May-23','To SQL']

# Lists to be filled with 30-minute swaths
jun23 = [0]*4
jan23 = [0]*4
feb23 = [0]*4
mar23 = [0]*4
apr23 = [0]*4
may23 = [0]*4

# Lists to be filled with day info
# [👕,🧼,💩,🍺,🍃,Caffeine,Work,💤]
days_info = [0]*8

# Put together list of possible Categories & Group types
ws = wb['Dropdown Backend']
all_cols = list(ws.columns)
options = []
for col in all_cols:
    for cell in col:
        if cell.value != None:
            options.append(cell.value)

categories = options[1:31]
groups = options[32:]

def process_col(month, col, min, max, index):
    output = []
    for cell in col:
        if max > 0 & min < 1:
            output.append(cell.value)
            max -= 1
            min -= 1
    month[index] = output

all_contents = []

# Process primary 30-minute swaths for every month from 'To SQL' up to end of 11-6-23
ws = wb['To SQL']
all_cols = list(ws.columns)
x = 0
for col in all_cols:
    if (x==0 or x==1 or x==2 or x==3):
        process_col(jan23, col, 0, 1200, x%5)
    if (x==5 or x==6 or x==7 or x==8):
        process_col(feb23, col, 0, 1344, x%5)
    if (x==10 or x==11 or x==12 or x==13): 
        process_col(mar23, col, 0, 1488, x%5)
    if (x==15 or x==16 or x==17 or x==18):
        process_col(apr23, col, 0, 1440, x%5)
    if (x==20 or x==21 or x==22 or x==23):
        process_col(may23, col, 0, 1488, x%5) 
    if (x==25 or x==26 or x==27 or x==28):
        process_col(jun23, col, 0, 528, x%5)
    x += 1
    
# Process additional info collected daily from 'Month Nav' up to end of May
ws = wb['Month Nav']
all_cols = list(ws.columns)
x = 0
for col in all_cols:
    if x==83:
        process_col(days_info, col, 8, 164, 6)
    if x==84:
        process_col(days_info, col, 8, 164, 0)
    if x==85:
        process_col(days_info, col, 8, 164, 1)
    if x==86:
        process_col(days_info, col, 8, 164, 2)
    if x==87:
        process_col(days_info, col, 8, 164, 3)
    if x==88:
        process_col(days_info, col, 8, 164, 4)
    if x==89:
        process_col(days_info, col, 8, 164, 5)
    if x==90:
        process_col(days_info, col, 33, 164, 7)
    x += 1

# Still need to add in Pages Read + Bed time

# print(all_contents)
# re.findall(r'([1-9]*[-][1-9]*[-][1-9]*)\w', all_contents)