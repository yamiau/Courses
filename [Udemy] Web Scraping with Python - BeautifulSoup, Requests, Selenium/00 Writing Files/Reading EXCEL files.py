import xlrd 

'''open workbook'''
workbook = xlrd.open_workbook('first_file.xlsx')


'''get sheet method - sheet_by_index(index)'''
worksheet = workbook.sheet_by_index(0)


'''find total number of rows'''
rows = worksheet.nrows


'''read rows - row_values(row_num)'''
#returns a tuple

for row in range(rows):
	first_col, second_col = worksheet.row_values(row)
	print(first_col, " 	", int(second_col))

