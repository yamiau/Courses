#Positional averages

def median(values):
	sort =  lambda v: v and [i for i in v[1:] if i < v[0]] + [v[0]] + [i for i in v[1:] if i > v[0]]
	values = sort(values)
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
	
mine = [100, 20, 11, 53, 67, 80]
print(median(mine))