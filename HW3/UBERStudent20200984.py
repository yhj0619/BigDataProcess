#!/usr/bin/python3

import sys
import calendar

with open(sys.argv[1], "rt") as f:
	uber_dict = dict()
	days=['MON','TUE','WED','THU','FRI','SAT','SUN']

	for line in f:
		text = line.split(",")

		date = text[1].split("/")
		eng_day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))

		key = text[0] + "," + days[eng_day]

		if key not in uber_dict:
			uber_dict[key] = text[2] + "," + text[3]
		else:
			new_list = uber_dict[key].split(",")
			v_sum = int(new_list[0]) + int(text[2])
			t_sum = int(new_list[1]) + int(text[3])
			uber_dict[key] = str(v_sum) + "," +str(t_sum)

with open(sys.argv[2], "wt") as f:
	for i in uber_dict.keys():
		f.write("%s %s\n" % (i, uber_dict[i]))
