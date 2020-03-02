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

def median2(values, frequencies):
	merged_set = [(values[i], frequencies[i]) for i in range(len(values))]
	merged_set = quick_sort2(merged_set)
	cumulative_freq =[]
	for i in range(len(merged_set)):
		if i > 0:
			cumulative_freq.append(merged_set[i][1] + cumulative_freq[i-1])
		else:
			cumulative_freq.append(merged_set[i][1])
	c = cumulative_freq[-1]/2
	for i in range(len(cumulative_freq)):
		if cumulative_freq[i] >= c:
			return merged_set[i][0]
	
def mode(values):
	s = [[i, 0] for i in set(values)]
	for i in s:
		for j in values:
			if i[0] == j:
				i[1] += 1 
	pivot = 0
	greatest = s[0][1]
	for i in range(len(s)):
		if s[i][1] > greatest:
			greatest = s[i][1]
			pivot = i
	return s[pivot][0]

def mode2(values, frequencies):
	pivot = 0
	greatest = frequencies[pivot]
	for i in range(len(frequencies)):
		if frequencies[i] > greatest:
			greatest = frequencies[i]
			pivot = i
	return values[pivot]
	
def quick_sort(values):	
	if values:
		pivot = values[0]
		smaller = [i for i in values[1:] if i < pivot]
		greater = [i for i in values[1:] if i >= pivot]
		return quick_sort(smaller) + [pivot] + quick_sort(greater)
	else:
		return(values)

def quick_sort2(values):
	if values:
		pivot = values[0][0]
		smaller = [i for i in values[1:] if i[0] < pivot]
		greater = [i for i in values[1:] if i[0] >= pivot]
		return quick_sort2(smaller) + [values[0]] + quick_sort(greater)
	else:
		return(values)
#
	
values = [1, 6, 88, 10, 35]
frequencies = [50, 26, 2, 31, 5]

print(mode2(values, frequencies))