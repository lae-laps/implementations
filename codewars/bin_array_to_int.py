def binary_array_to_number(arr):
    length = len(arr)
    total = 0
    count = 0
    for i in arr:
        total += (2 ** (length - (count + 1))) * i
        count += 1
    return total
