#!/usr/bin/python3

import sys

with open(sys.argv[1], "rt") as f:
	genre_dict = {}
	dict_no_dup = dict()
	result_dict = {}
	result={}
	data = f.read()
	lines = data.split("\n")
	with open(sys.argv[2],"wt") as f1:
		for line in lines:
			movie = line.split("::")
			genres = movie[2]
			genre = genres.split("|")
			for genre_title in genre:
				if genre_title not in genre_dict:
					genre_dict[genre_title] = 1
				else:
					genre_dict[genre_title] += 1
		keyList=genre_dict.keys()
		for i in keyList:
			f1.write('%s %d\n' % (i, genre_dict[i]))
