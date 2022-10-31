#!/usr/bin/python3

import sys

with open(sys.argv[1], "rt") as f:
	genre_dict = {}
	dict_no_dup = dict()
	result_dict = {}
	
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
			for key, val in genre_dict.items():
				dict_no_dup[val] = key
			for key, val in dict_no_dup.items():
				result_dict[val] = key
		for k, v in result_dict.items():
			f1.write('{} {}\n'.format(k,v))
