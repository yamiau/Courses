#Positional averages

def median(values):
	sort =  lambda v: v and sort([i for i in v[1:] if i < v[0]]) + [v[0]] + sort([i for i in v[1:] if i > v[0]])
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
	sort = lambda v: v and sort([i for i in v[1:] if i[0] < v[0][0]]) + [v[0]] + sort([i for i in v[1:] if i[0] > v[0][0]])
	merged_set = sort(merged_set)
	cumulative_freq = []
	accumulate = lambda x, y: x.append(y[i][1]) if i == 0 else x.append(y[i][1] + x[i-1]) for i in range(len(y))
	accumulate(cumulative_freq, merged_set)
	print(cumulative_freq)
#	for i in range(len(merged_set)):
#		if i > 0:
#			cumulative_freq.append(merged_set[i][1] + cumulative_freq[i-1])
#		else:
#			cumulative_freq.append(merged_set[i][1])
#	c = cumulative_freq[-1]/2
#	for i in range(len(cumulative_freq)):
#		if cumulative_freq[i] >= c:
#			return merged_set[i][0]
	
def mode(oneD):
	copy = oneD
	for i in oneD:
		copy.append(i)
		
	return(None)
	
mine = [100, 20, 11, 53, 67, 80]
freqs = [3, 53, 68, 12, 2, 45]
median2(mine, freqs)