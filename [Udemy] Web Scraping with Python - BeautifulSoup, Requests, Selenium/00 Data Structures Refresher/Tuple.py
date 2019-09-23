'''TUPLES'''

my_tuple = 'Yami', 25, 'black' 	#boxing/packing
name, age, eye_color = my_tuple 	#unboxing/unpacking

print(my_tuple)
print(name)
print(age)
print(eye_color)

person = 'Claire', 19, ('brown', 'pink')	#nested tuples
print(person[2])
print((person[2])[0])
print((person[2])[1])


'''
Tuples are immutable
	for value in my_tuple:
		print(value)
		
Tuples are iterable

Tuples can be nested

Values can be repeated through multiplication
	my_tuple = ('thrice',) *3
	<>
	my_tuple = ('thrice') *3
		the latter will be declared as a string
'''

