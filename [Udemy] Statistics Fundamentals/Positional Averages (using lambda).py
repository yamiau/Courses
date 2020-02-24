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

def median2(values, frequencies):
	merged_set = [(values[i], frequencies[i]) for i in range(len(values))]
	print(merged_set)
	sort = lambda v: v and [i for i in v[1:] if i[0] < v[0][0]] + [v[0][0]] + [i for i in v[1:] if i[0] > v[0][0]]
	merged_set = sort(merged_set)
	print(merged_set)
	
def mode(oneD):
	copy = oneD
	for i in oneD:
		copy.append(i)
		
	return(None)
	
mine = [100, 20, 11, 53, 67, 80]
freqs = [3, 53, 68, 12, 2, 45]
median2(mine, freqs)