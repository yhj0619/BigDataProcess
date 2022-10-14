#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook( "student.xlsx" )
ws = wb['Sheet1']


row_id = 1
total_list = []
total_sort = []
str_grade = ['A+','A0','B+','B0','C+','C0']

for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row=row_id, column = 7).value = sum_v
		total_list.append(sum_v)
	row_id += 1

total_sort= sorted(total_list,reverse=True)

student = 0

row_id_new = 1
for row in ws:
	if row_id_new != 1:
		if len(total_sort) * 0.3:
			ws.cell(row=row_id_new, column=8).value = 'A0'
	row_id_new += 1	
 
		





wb.save( "student.xlsx" )
