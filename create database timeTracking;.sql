create database timeTracking;
use timeTracking;

create table granularData (
		t1 Date,
        t2 Day,
        t3 Time,
        timezone varchar(5),
        category varchar(255),
        deltaMoney money,
        audience varchar(255),
        descr varchar(8000)
);

create table dailyData (
        t1 Date,
        t2 Day,
        sleep float DEFAULT 0,
        workTime float DEFAULT 0,
        laundry bit DEFAULT 0,
        shower bit DEFAULT 0,
        poop int DEFAULT 0,
        a int DEFAULT 0,
        w int DEFAULT 0,
        summary varchar(8000)
);