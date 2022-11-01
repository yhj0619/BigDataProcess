#!/usr/bin/python3

import sys
import calendar

with open(sys.argv[1], "rt") as f:
	uber_dict = dict()
	days=['MON','TUE','WED','THU','FRI','SAT','SUN']
	data = f.read()
	lines = data.split("\n")

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
		eng_day = calendar.weekday(y,m,d)

		key = region + "," + days[eng_day]

		if key not in uber_dict:
			uber_dict[key] = vehicles + "," + trips
		else:
			new_list = uber_dict[key].split(",")
			v_sum = int(new_list[0]) + int(vehicles)
			t_sum = int(new_list[1]) + int(trips)
			uber_dict[key] = str(v_sum) + "," +str(t_sum)

with open(sys.argv[2], "wt") as f:
	for k, v in uber_dict.items():
		f.write("%s %s\n" % (k, v))
