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
