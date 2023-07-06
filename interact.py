"""
create table granularData (t1 Date, t2 Day, t3 Time, timezone varchar(5), category varchar(255), deltaMoney money, audience varchar(255), descr varchar(8000));
create table dailyData (t1 Date, t2 Day, sleep float DEFAULT 0, workTime float DEFAULT 0, laundry bit DEFAULT 0, shower bit DEFAULT 0, poop int DEFAULT 0, a int DEFAULT 0, w int DEFAULT 0, summary varchar(8000));
);
"""

import psycopg2;
import psycopg2.extras;
import creds;

# Run command and commit to db
def run(message):
    cur.execute(message)
    conn.commit()

#   print out contents SELECTed
def display(message):
    cur.execute(message)
    print(cur.fetchall())

creds = creds.creds

conn = psycopg2.connect(dbname=creds["dbname"], 
                 user=creds["user"], 
                 password=creds["password"], 
                 host=creds["host"])

cur = conn.cursor()

run("create table granularData (t1 Date, t2 VARCHAR(10), t3 Time, timezone VARCHAR(5), category VARCHAR(255), deltaMoney money, audience VARCHAR(255), descr VARCHAR(8000));")
run("create table dailyData (t1 Date, t2 VARCHAR(10), sleep float DEFAULT 0, workTime float DEFAULT 0, laundry int DEFAULT 0, shower int DEFAULT 0, poop int DEFAULT 0, a int DEFAULT 0, w int DEFAULT 0, summary VARCHAR(8000));")

conn.close()