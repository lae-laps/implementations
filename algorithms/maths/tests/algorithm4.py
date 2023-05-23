u = [10, 15, 9, 7, 11]

n = 1
a = u[n - 1]
while n < 5:
    n += 1
    t = u[n - 1]
    if t < a:
        a = t

print(a)

