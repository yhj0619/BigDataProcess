#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook( "student.xlsx" )
ws = wb['Sheet1']


row_id = 1
total_list = []
total_sort = []

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

row_new = 1
for row in ws:
	if row_new != 1:
		for n in total_sort:
			A_cnt = int(len(total_sort) * 0.3)
			B_cnt = int(len(total_sort)*0.7) - A_cnt
		
			for i in range(A_cnt):
				if ws.cell(row=row_new, column=7).value == total_sort[i]:
					ws.cell(row=row_new, column=8).value = 'A0'	
			
			for i in range(A_cnt,A_cnt+ B_cnt):
				if ws.cell(row=row_new, column=7).value == total_sort[i]:
					ws.cell(row=row_new,column=8).value ='B0'

			for i in range(A_cnt+B_cnt,len(total_sort)):
				if ws.cell(row=row_new, column=7).value == total_sort[i]:
					ws.cell(row=row_new,column=8).value = 'C0'

	row_new += 1

wb.save( "student.xlsx" )
