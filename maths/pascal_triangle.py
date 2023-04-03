# pascal triangle calculator

import sys
import math

rows = 15

if len(sys.argv) > 1:
    try:
        rows = int(sys.argv[1])        
    except Exception:
        pass

buffer = []

for i in range(rows):
    tmp = []
    for j in range(i + 1):
        if j == 0 or i == 0:
            tmp.append(1)
        else:
            tmp.append(buffer[i - 1][j - 1] + buffer[i - 1][j])
    tmp.append(0)
    buffer.append(tmp)

# display the triangle

max_len = len(str(buffer[len(buffer) - 1][len(buffer) // 2]))   # maximum possible length

for i in range(len(buffer)):
    for j in range((rows - i) * max_len + 1):
        print(' ', end='')

    for j in buffer[i]:
        if j != 0:
            #print(f"{j} ", end=' ')
            for _ in range((max_len - len(str(j)) + max_len) // 2): 
                print(' ', end='')
            print(j, sep='', end='')
            for _ in range((max_len - len(str(j)) + max_len) // 2 + math.ceil((max_len - len(str(j)) + max_len) % 2)): 
                print(' ', end='')

    print()


