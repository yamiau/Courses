#Mathematical averages
	
import math

def arithmetic_mean(values):
	total = 0
	for i in values:
		total += i
	result = total/len(values)
	return(result)
	
def arithmetic_mean2(values, frequencies):
	total= 0
	for i in range(0, len(values)):
		total += values[i] * frequencies[i]
	observations = 0
	for i in frequencies:
		observations += i; 
	result = total/observations
	return(result)
		
def geometric_mean(values):
	total = 1
	for i in values:
		total *= i
	exp = 1/len(values)
	result = math.pow(total, exp)
	return(result)	
	
def geometric_mean2(values, frequencies):
	for i in values:
		if i <= 0:
			return("GM not achievable!")
	
	total = 1
	for i in range(0,len(values)):
		total *= math.pow(values[i], frequencies[i])
	exp = 1/len(values)
	result = math.pow(total, exp)
	return(result)		

def harmonic_mean(oneD):
	total = 0
	for i in oneD:
		total += i
	result = (total/len(oneD))
	return(result)

#Positional averages

def median(values):
	values = quick_sort(values)
	if (len(values)%2) == 0:
		index = int(len(values)/2)
		result = (values[index] + values[index-1])/2
		return(result)
	else:
		index = (int(len(values)/2))
		return(values[index])
	
def mode(oneD):
	copy = oneD
	for i in oneD:
		copy.append(i)
		
	return(None)
	
#Supporting methods
	
def quick_sort(values):
	if values:
		pivot = values[0]
		smaller = [i for i in values[1:] if i < pivot]
		greater = [i for i in values[1:] if i >= pivot]
		return quick_sort(smaller) + [pivot] + quick_sort(greater)
	else:
		return(values)
	
mine = [10, 20, 11, 53, 67, 80]
print(quick_sort(mine))
print(median(mine))