from xlsxwriter import Workbook

'''make workbook'''
workbook = Workbook('first_file.xlsx')

'''add worksheet'''
worksheet = workbook.add_worksheet()

'''write - function(row, column, value)'''

#worksheet.write(0, 0, "row zero col zero")
#worksheet.write(0, 1, "row zero col one")
#worksheet.write(1, 0, "row one col zero")
#worksheet.write(1, 1, "row one col one")

for row in range(0,20):
	worksheet.write(row, 0, "row num")
	worksheet.write(row, 1, row)


'''close workbook'''
workbook.close()