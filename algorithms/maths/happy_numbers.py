# Take an integer n. Square its digits and add them, repeat this untill the answer is 1 or you get stuck in a loop
# if the answer is 1 the number is happy, otherwise it is not.

def is_happy(n):
   
    # Function checks given an integer whether it is happy or not
    # Returns true or false and a buffer with all the steps to get there

    count = 0
    buffer = [n]

    while True:
        t = 0
        for c in str(buffer[count]):
            t += int(c) ** 2

        if t == 1:
            buffer.append(t)
            return True, buffer
        
        if t in buffer:
            buffer.append(t)
            return False, buffer

        buffer.append(t)

        count += 1

# Iterate through the first 100 integers and see wether each one is happy

for i in range(10000000):
    check, buffer = is_happy(i)

    if check:
        print(f"# {i} >> ", end='')
    else:
        print(f"  {i} >> ", end='')
    for j in buffer:
        print(f" , {j}", end='')

    print()

