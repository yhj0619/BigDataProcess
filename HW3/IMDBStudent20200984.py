#!/usr/bin/python3
import sys

with open(sys.argv[1], "rt") as f:
	genre_dict = {}
	data = f.read()
	lines = data.split("\n")
	with open(sys.argv[2], "wt") as f1:
		for line in lines:
			movie = line.split("::")
			genres = movie[2]
			genre = genres.split("|")
			for genre_title in genre:
				if(genre_title in genre_dict) == False:
					genre_dict[genre_title] = 1
				else:
					genre_dict[genre_title] += 1
			f1.write('{} {}\n'.format(genre_title, genre_dict[genre_title]))
