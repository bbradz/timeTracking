import datetime

"""(t1 Date, 
    t2 VARCHAR(10),
    sleep float DEFAULT 0, 
    workTime float DEFAULT 0, 
    laundry int DEFAULT 0, 
    shower int DEFAULT 0, 
    poop int DEFAULT 0, 
    a int DEFAULT 0, 
    w int DEFAULT 0, 
    summary VARCHAR(8000))"""

def add_days_info():
    day = datetime.date(2023, 1, 7)
    d = datetime.timedelta(days=1)
    for i in range(179):
        print(str(day))
        print(str(day.strftime("%A")))
        day += d

        # message = f"INSERT INTO \"dailydata\" (t1, t2, sleep, worktime, laundry, shower, poop, a, w, summary) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {});"
        # run(message)

add_days_info() 