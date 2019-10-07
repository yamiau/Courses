import matplotlib.pyplot as plt
import random

vector = [random.randint(-1000,1000) for i in range(100)]

plt.boxplot(vector)
plt.title("Boxplot example")
plt.show()

