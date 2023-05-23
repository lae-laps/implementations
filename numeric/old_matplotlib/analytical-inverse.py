import math
import matplotlib.pyplot as plt

max_n = 100
base_count = 2
increase_rate = 0.1

def log(base, x):
    results = []
    log = math.log(x, base)
    return log

count = base_count
base_array = []
while count <= max_n:
    base_array.append(count)
    count += increase_rate

for i in range(2, 3):
    count = base_count
    plot = []
    while count <= max_n:
        print(count)
        plot.append(log(count, i))
        #print(plot)
        count += increase_rate

    plt.plot(base_array, plot)

print(f"base: {len(base_array)}\nplot : {len(plot)}\n")

print(f"plot : {plot}")


plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.show()

