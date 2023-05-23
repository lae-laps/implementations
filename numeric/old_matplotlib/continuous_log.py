import math
import matplotlib.pyplot as plt

max_n = 12 
increase_rate = 0.1

count = 0
base_array = []
while count < max_n:
    count += increase_rate
    base_array.append(count)

plot = []

for base in base_array:
    plot.append(math.log(base * base, 10))

plt.plot(base_array, plot)

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.show()

