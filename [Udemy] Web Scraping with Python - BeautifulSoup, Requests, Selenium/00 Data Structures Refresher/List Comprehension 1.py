'''Generating a list automatically'''

import random
#random.randint(inclusive, inclusive)

my_list = []
for value in range(0, 20):
	my_list.append(random.randint(0, 100))
	
print(my_list)
print(len(my_list))

new_list = [value for value in range(0, 20)] #produces a linear list
print(new_list)

newer_list = [random.randint(0,100) for value in range(0,20)]
print(newer_list)