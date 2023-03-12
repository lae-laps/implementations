increment = 0.001

base = 0
for i in range(100):
    base_constant = (base ** increment) / increment
    print(f"base: {base} | constant: {base_constant}")
    base += 0.1

