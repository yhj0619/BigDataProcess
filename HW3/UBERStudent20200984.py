#!/usr/bin/python3

import sys
import datetime

with open(sys.argv[1], "rt") as f:
	uber_dict = {}
	v_sum = 0
	t_sum = 0
	days=['MON','TUE','WED','THU','FRI','SAT','SUN']
	data = f.read()
	lines = data.split("\n")
	with open(sys.argv[2],"wt") as f1:
		for line in lines:
			text = line.split(",")
			region = text[0]
			day = text[1]
			vehicles = int(text[2])
			trips = int(text[3])
			date = day.split("/")
			m = int(date[0])
			d = int(date[1])
			y = int(date[2])
			str_day = days[datetime.date(y,m,d).weekday()]
			new_key = region + "," + str_day
			if new_key not in uber_dict:
				new_value = str(vehicles) + "," + str(trips)
				uber_dict[new_key] = new_value
			else:
				v_sum += vehicles
				t_sum += trips
				new_value = str(v_sum) + "," + str(trips)
				uber_dict[new_key] = new_value
		for i in uber_dict:
			f1.write('%s %s\n' % (i, uber_dict[i]))
