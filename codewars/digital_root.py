def digital_root(n):
    while len(str(n)) > 1:
        count = 0
        for digit in iter(str(n)):
            count += int(digit)
        n = count
    return n
