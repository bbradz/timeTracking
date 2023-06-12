from openpyxl import load_workbook
import re

data_file = '/Users/benbradley/Downloads/Current Time Tracking 🗓️.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file)

# Lists to be filled with cell contents
jun23 = []
jan23 = []
feb23 = []
mar23 = []
apr23 = []
may23 = []

sheetNames = ['June-23','Month Nav','Week Template','Dropdown Backend','Ideas...','Jan-23','Feb-23','Mar-23','Apr-23','May-23']

# List all the sheets in the file.
print("Found the following worksheets:")

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
print(categories)
print(groups)

all_contents = []
for sheetname in wb.sheetnames:
    print(sheetname)
    if sheetname == 'To SQL':
        ws = wb['To SQL']
        all_cols = list(ws.columns)
        for col in all_cols:
            for cell in col:
                print(cell.value)


# print(all_contents)
# re.findall(r'([1-9]*[-][1-9]*[-][1-9]*)\w', all_contents)

"""  
for sheetname in wb.sheetnames:
    ws = wb[sheetname]
    all_cols = list(ws.columns)
    for col in all_cols:
        for cell in col:
            print(cell.value) """

