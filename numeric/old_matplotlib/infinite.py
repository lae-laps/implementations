import math
import matplotlib.pyplot as plt

max_n = 60
increase_rate = 0.1

def log_plot(base):
    results = []
    
    x = 0
    while x <= max_n:
        x += increase_rate
        log = math.log(x, base)
        results.append(log)
    
    return results

count = 0
base_array = []
while count < max_n:
    count += increase_rate
    base_array.append(count)

count = 2
while count <= max_n:
    print(count)
    plot = log_plot(count)
    print(plot)
    plt.plot(base_array, plot)
    count += increase_rate

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.show()

