import math
import matplotlib.pyplot as plt

do = 261.63
mi = 330.0
sol = 392.0

pi = 3.141592653

min_n = 0
max_n = 0.05
increase_rate = 0.00000005

def func(x):
    return math.sin(x)

count = min_n
base_array = []
while count <= max_n:
    base_array.append(count)
    count += increase_rate

plot = []
for t in base_array:
    plot.append(func(2 * pi * do * t) + (func(2 * pi * sol * t) * 0.5) + (func(2 * pi * mi * t) * 0.3) + (func(2 * pi * (do * 2) * t) * 0.2))

plt.plot(base_array, plot)

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.show()

