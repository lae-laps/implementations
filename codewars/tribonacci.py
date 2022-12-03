def tribonacci(signature, n):
    if n <= 0:
        return []
    elif n <= 3:
        return signature[0:n]
    a = signature[0]
    b = signature[1]
    c = signature[2]
    for _ in range(n - 3):
        x = a + b + c
        a = b
        b = c
        c = x
        signature.append(x)
    return signature
