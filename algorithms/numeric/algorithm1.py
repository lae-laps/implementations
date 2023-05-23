n = 1
a = 1
b = 1

print(a, b)

while n < 5:
    c = a + b

    print(c)

    n += 1

    a = b

    b = c

