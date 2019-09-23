a = 20
if a == 20:
	print('a is 20')
else:
	print('a is not 20')


'''Using in-line if else statements'''

print('a is 20' if a == 20 else 'a is not 20')
b = True if a == 20 else False
print(b) 
#true condition else false


'''Using in-line if else statements in list comprehension'''
num = [value for value in range(-5, 5)]
print(num)

pos_num = [value for value in num if value >= 0]
print(pos_num)