import iniconfig
from openpyxl import load_workbook
import re

def extract():
    data_file = '/Users/benbradley/Downloads/Current Time Tracking 🗓️.xlsx'
    
    # Load the entire workbook.
    wb = load_workbook(data_file)

    # List all the sheets in the file.
    sheetNames = ['June-23','Month Nav','Week Template','Dropdown Backend','Ideas...','Jan-23','Feb-23','Mar-23','Apr-23','May-23','To SQL']

    # [Category, DeltaMoney, Who?, Details]
    # Lists to be filled with 30-minute swaths
    jun23 = [0]*4
    jan23 = [0]*4
    feb23 = [0]*4
    mar23 = [0]*4
    apr23 = [0]*4
    may23 = [0]*4

    # Lists to be filled with day info
    # [👕,🧼,💩,🍺,🍃,Caffeine,💤,Work,Summary]
    days_info = [0]*9

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

    def process_col(month, col, min, max, index, cut):
        output = []
        x = 1
        for cell in col:
            if (x > min and x < max+1):
                    output.append(cell.value)
            x += 1
        month[index] = output

    # Process primary 30-minute swaths for every month from 'To SQL' up to end of 11-6-23
    ws = wb['To SQL']
    all_cols = list(ws.columns)
    x = 0
    for col in all_cols:
        if (x==0 or x==1 or x==3):
            process_col(jan23, col, 0, 1200, x%5, True)
        if (x==2):
            process_col(jan23, col, 0, 1200, x%5, False)
        if (x==5 or x==6 or x==8):
            process_col(feb23, col, 0, 1344, x%5, True)
        if (x==7):
            process_col(feb23, col, 0, 1344, x%5, False)
        if (x==10 or x==11 or x==13): 
            process_col(mar23, col, 0, 1488, x%5, True)
        if (x==12):
            process_col(mar23, col, 0, 1488, x%5, False)
        if (x==15 or x==16 or x==18):
            process_col(apr23, col, 0, 1440, x%5, True)
        if (x==17):
            process_col(apr23, col, 0, 1440, x%5, False)
        if (x==20 or x==21 or x==23):
            process_col(may23, col, 0, 1488, x%5, True) 
        if (x==22):
            process_col(may23, col, 0, 1488, x%5, False) 
        if (x==25 or x==26 or x==28):
            process_col(jun23, col, 0, 1440, x%5, True)
        if (x==27):
            process_col(jun23, col, 0, 1440, x%5, False)
        x += 1
        
    # Process additional info collected daily from 'Month Nav' up to end of May
    ws = wb['Month Nav']
    all_cols = list(ws.columns)
    x = 0
    for col in all_cols:
        if x==83:
            # 187 set to be updated to 2023-07-04
            process_col(days_info, col, 8, 187, 6, False)
        if x==84:
            process_col(days_info, col, 8, 187, 0, False)
        if x==85:
            process_col(days_info, col, 8, 187, 1, False)
        if x==86:
            process_col(days_info, col, 8, 187, 2, False)
        if x==87:
            process_col(days_info, col, 8, 187, 3, False)
        if x==88:
            process_col(days_info, col, 8, 187, 4, False)
        if x==89:
            process_col(days_info, col, 8, 187, 5, False)
        if x==90:
            process_col(days_info, col, 33, 187, 7, False)
        x += 1

    # Compile all the summaries from each of the month
    def getSummary(table):
        ws = wb[table]
        all_cols = list(ws.columns)
        options = []
        for col in all_cols:
            for cell in col:
                if cell.value != None:
                    if ("Summary:" in str(cell.value)):
                        if (str(cell.value) == 'Summary: '):
                            result = "no summary available"
                        else:
                            result = re.sub('Summary: ','', str(cell.value))
                        options.append(result)
        return options
    janSummary = ["No summaries for Jan"]*29
    summaries = janSummary+getSummary('Feb-23')+getSummary('Mar-23')+getSummary('Apr-23')+getSummary('May-23')+getSummary('Jun-23')
    days_info[8] = summaries

    # Haven't included Pages Read + Bed time
    # re.findall(r'([1-9]*[-][1-9]*[-][1-9]*)\w', all_contents)
    return jan23, feb23, mar23, apr23, may23, jun23, days_info