import sys

# This algorithm is super unefficient, its just a cool trick to implement

sys.setrecursionlimit(1000) # Its so unefficient, we have to artificially increment the max recursion limit

def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    return 1

for i in range(134):
    print(f"{i:3}! : {factorial(i)}")

