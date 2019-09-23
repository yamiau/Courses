'''Nested lists'''

carts = [['toothpaste', 'soap', 'toilet paper'], ['meat', 'fruit', 'cereal'], ['pencil', 'notebook', 'eraser']]
#or 
person1 = ['toothpaste', 'soap', 'toilet paper']
person2 = ['meat', 'fruit', 'cereal']
person3 = ['pencil', 'notebook', 'eraser']
carts = [person1, person2, person3]

print(carts)

for value in carts:
	print(value)

#print(my_list[row][column])

'''2D list'''

my_matrix = []

#range(start inclusive, stop exclusive, step)
for row in range(0, 25, 5):
	row_list = []
	for column in range(row, row+5):
		row_list.append(column)
	my_matrix.append(row_list)	

print(my_matrix)

for row in my_matrix:
	print(row)
	
'''Using list comprehension'''

new_matrix = [[column for column in range(row, row+5)] for row in range(0,25,5)]
print(new_matrix)