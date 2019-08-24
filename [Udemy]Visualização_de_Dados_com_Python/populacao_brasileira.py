#Crescimento da população brasileira 1980-2018
#DataSus+IBGE

import matplotlib.pyplot as plt

data = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(1, len(data)):
		line = data[i].split(";")
		x.append(int(line[0]))
		y.append(int(line[1]))

plt.plot(x, y, color = 'g')
plt.bar(x, y, color = '#f0f0b0')
plt.grid(True, ls = '--')
plt.title("Crescimento da população brasileira 1980-2018")
plt.xlabel("Ano")
plt.ylabel("População (100mi)")
plt.show
plt.savefig("crescimento_populacao_br.png", dpi = 300)