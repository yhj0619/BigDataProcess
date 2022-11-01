#!/usr/bin/python3

import sys
import datetime

with open(sys.argv[1], "rt") as f:
	uber_dict = {}
	days=['MON','TUE','WED','THU','FRI','SAT','SUN']
	data = f.read()
	lines = data.split("\n")
	with open(sys.argv[2],"wt") as f1:
		for line in lines:
			text = line.split(",")
			region = text[0]
			day = text[1]
			vehicles = text[2]
			trips = text[3]
			date = day.split("/")
			m = int(date[0])
			d = int(date[1])
			y = int(date[2])
			str_day = days[datetime.date(y,m,d).weekday()]
			new_key = region + "," + str_day
			new_value = vehicles + "," + trips
			f1.write('%s %s\n' % (new_key, new_value))

