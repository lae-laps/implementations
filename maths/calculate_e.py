# Program to aproximate eulers number

iterations = 100

for i in range(1, iterations + 1):
    e = (1 + (1 / i)) ** i
    print(f"{i}: {e}")

