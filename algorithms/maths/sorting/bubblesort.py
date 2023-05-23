# bubblesort implementation in python

buffer = [1, 4, 67, 87, 4, 34, 5, 9, 8, 5, 21]

def bubblesort_increasing(buffer):

    # bubblesort in increasing order

    n = len(buffer)

    check = False                                                       # optimization if the array is already ordered

    for i in range(n - 1):
        for j in range(n - i - 1):
            if buffer[j] > buffer[j + 1]:
                check = True
                buffer[j], buffer[j + 1] = buffer[j + 1], buffer[j]     # swap the elements
        if not check:                                                   # check whether we have made any changes, if not, we can just return
            return buffer
    return buffer

def bubblesort_decreasing(buffer):

    # bubblesort in decreasing order

    n = len(buffer)                                                     # also precalculating this means we only have to calculate it once

    check = False

    for i in range(n - 1):
        for j in range(n - i - 1):
            if buffer[j] < buffer[j + 1]:                               # this is the only line that changes
                check = True
                buffer[j], buffer[j + 1] = buffer[j + 1], buffer[j]
        if not check:
            return buffer
    return buffer

def bubblesort_single_loop(buffer):
    n = len(buffer)

    for i in range(n * n + ( -i - 2 ) * n + i + 1):
        # continue here


print(buffer)
print(bubblesort_increasing(buffer))
print(bubblesort_decreasing(buffer))

