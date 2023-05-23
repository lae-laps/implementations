# This program aproximates the infinite series from the basilea series which aproximates to pi^2/6

MAX = 1000

total = 0.0

for x in range(1, MAX):
    total += 1 / (x * x)

print(total)

