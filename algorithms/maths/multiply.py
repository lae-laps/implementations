def multiply(a, b):

    col_1 = [a]
    col_2 = [b]

    while True:
        
        col_1.append(col_1[len(col_1) - 1] // 2)
        col_2.append(col_2[len(col_2) - 1] *  2)

        if col_1[len(col_2) - 1] == 1:
            break

    total = 0
    for i in range(len(col_1)):
        if col_1[i] % 2 != 0:
            total += col_2[i]

    return total, col_1, col_2

for i in range(10, 100):
    for j in range(10, 100):
        x, a, b = multiply(i, j)
        print(f"{i} x {j} = {x} : {a} {b}")


