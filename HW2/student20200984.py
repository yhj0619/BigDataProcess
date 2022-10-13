#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook( "20200984.xlsx" )
ws = wb['Sheet1']

row_id = 1;
for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value *0.3
	row_od += 1

wb.save( "20200984.xlsx" )


