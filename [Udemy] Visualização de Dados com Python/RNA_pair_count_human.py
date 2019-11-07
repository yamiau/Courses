#RNA Nucleotide pairing comparison between Homo sapiens and Escherichia colli

nucleotides = ["A", "T", "C", "G"]

genome_in = open("human.fasta").read()
genome_out = open("human.html", "w")
genome_in = genome_in.replace("\n", "")

count = {}

for i in nucleotides:
	for j in nucleotides:
		count[i+j] = 0
		
for i in range(len(genome_in) -1):
	count[genome_in[i] + genome_in[i+1]] += 1
	
print(count)

k = 1
for i in count:
	opacity = count[i]/max(count.values())
	genome_out.write("<div style = 'width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, %s')>%s</div>" % (str(opacity), i) )
 
	if k%4 == 0:
		genome_out.write("<div style='clear:both'></div>")  
	
	k += 1
	
genome_out.close()