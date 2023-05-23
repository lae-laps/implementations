import math
import matplotlib.pyplot as plt

max_n = 12 
increase_rate = 0.1

def log_plot(base):
    results = []
    
    x = 0
    while x < max_n:
        x += increase_rate
        log = math.log(x, base)
        results.append(log)
    
    return results

e = 2.718281828459045

base_2  = log_plot(2)
base_e  = log_plot(e)
base_10 = log_plot(10)

print(f"log 2 : {base_2}")
print(f"log e : {base_e}")
print(f"log 10 : {base_10}")

base_array = []

count = 0
while count < max_n:
    count += increase_rate
    base_array.append(count)

plt.plot(base_array, base_2)
plt.plot(base_array, base_e)
plt.plot(base_array, base_10)

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.show()

