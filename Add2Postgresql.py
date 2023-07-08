import psycopg2;
import psycopg2.extras;

import ExcelExtracting;
import math;
import datetime;

import re;
from cleantext import clean;

import sys;
import os;
creds_file = "/Users/benbradley/Downloads"
path = os.path.abspath(creds_file)
sys.path.append(path)
import creds;
creds = creds.creds


#   Run command and commit to db
def run(message):
    cur.execute(message)
    conn.commit()
#   print out contents SELECTed
def display(message):
    cur.execute(message)
    print(cur.fetchall())
#   make a string acceptable to varchar sql datatype
def trimString(string):
    string = clean(string, no_emoji=True)
    string = re.sub('@', 'at ', string)
    string = re.sub(r'[^A-Za-z0-9 ]+', '', string)
    string = re.sub(r"\s+", '_', string)
    return string;


#   insert 30-min slots for entire month into granulardata
days = ["\'monday\'", "\'tuesday\'", "\'wednesday\'", "\'thursday\'", "\'friday\'", "\'saturday\'", "\'sunday\'"]
def addGranularMonth(firstDayNum, lastDayNum, firstDayIndex, yearNum, monthNum, arr):
    for dayNum in range(firstDayNum,lastDayNum+1):
        dateString = f"\'{yearNum}-{monthNum}-{dayNum}\'"
        if (firstDayIndex % 7 == 0): firstDayIndex = 1
        dayString = days[firstDayIndex]
        for j in range(48):
            adjustedIndex = ((dayNum-firstDayNum)*48)+j
            timezone = "\'EST\'"
            category = f"\'{trimString(arr[0][adjustedIndex])}\'"
            deltaMoney = f"\'{arr[1][adjustedIndex]}\'"
            deltaMoney = re.sub('=','', deltaMoney)
            audience = f"\'{trimString(arr[2][adjustedIndex])}\'"
            descr = f"\'{trimString(arr[3][adjustedIndex])}\'"
            if (j % 2 == 1): 
                minute = "30" 
            else: minute = "00"
            time = f"\'{math.floor(j / 2)}.{minute}\'"
            message = f"INSERT INTO \"granulardata\" (t1, t2, t3, timezone, category, deltamoney, audience, descr) VALUES ({dateString}, {dayString}, {time}, {timezone}, {category}, {deltaMoney}, {audience}, {descr});"
            run(message)
        firstDayIndex += 1


#   insert daily collected datapoints for entire month into dailydata
def add_days_info(arr):
    day = datetime.date(2023, 1, 7)
    d = datetime.timedelta(days=1)
    # 179 set to be updated to 2023-07-04
    for i in range(179):
        sleep = f"\'{arr[6][i]}\'"
        laundry = f"\'{arr[1][i]}\'"
        shower = f"\'{arr[2][i]}\'"
        poop = f"\'{arr[3][i]}\'"
        a = f"\'{arr[4][i]}\'"
        w = f"\'{arr[5][i]}\'"
        dayName = trimString(day.strftime("%A")).lower()
        dayName = f"\'{dayName}\'"
        date = f"\'{str(day)}\'"
        summary = f"\'{trimString(arr[8][i])}\'"
        if i>25:
            worktime = f"\'{arr[7][i-26]}\'"
        else:
            worktime = f"\'0\'"
        message = f"INSERT INTO \"dailydata\" (t1, t2, sleep, worktime, laundry, shower, poop, a, w, summary) VALUES ({date}, {dayName}, {sleep}, {worktime}, {laundry}, {shower}, {poop}, {a}, {w}, {summary});"
        run(message)
        day += d


#   show table, enter in: '____' format not: "_____"
def show(table):
    cur.execute(f'SELECT * FROM {table};')
    for record in cur.fetchall():
        print(record)


#   Call ExcelExtracting and assign it to new variables
jan23, feb23, mar23, apr23, may23, jun23, days_info = ExcelExtracting.extract()
conn = None
cur = None
try:
    conn = psycopg2.connect(dbname=creds["dbname"], 
                    user=creds["user"], 
                    password=creds["password"], 
                    host=creds["host"])
    cur = conn.cursor()

    # addGranularMonth(7, 31, 5, 2023, 1, jan23); addGranularMonth(1, 28, 2, 2023, 2, feb23); addGranularMonth(1, 31, 2, 2023, 3, mar23); addGranularMonth(1, 30, 5, 2023, 4, apr23); addGranularMonth(1, 31, 0, 2023, 5, may23); addGranularMonth(1, 30, 3, 2023, 6, jun23);
    # add_days_info(days_info)

    # show('granularData')
    # show('dailyData')

    # run("delete from granularData;")
    # run("delete from dailyData;")

    # run("create table granularData (t1 Date, t2 VARCHAR(10), t3 VARCHAR(5), timezone VARCHAR(5), category VARCHAR(255), deltaMoney money, audience TEXT, descr TEXT);")
    # run("create table dailyData (t1 Date, t2 VARCHAR(10), sleep float DEFAULT 0, workTime float DEFAULT 0, laundry int DEFAULT 0, shower int DEFAULT 0, poop int DEFAULT 0, a int DEFAULT 0, w int DEFAULT 0, summary TEXT);")

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()