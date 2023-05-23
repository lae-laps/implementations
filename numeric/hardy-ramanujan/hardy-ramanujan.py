# This algorithm calculates Hardy-Ramanujan's number
# This is the smallest number that can be expressed as the sum of two positive cubes in two different ways
# 1729
# 1729 = 1^3 + 12^3 = 9^3 = 10^3
# This script is also extensible to find numbers to other powers by changing the value POWER

from datetime import datetime

LOGFILE = "./results.txt"

POWER = 3
MAX_MAGNITUDE = 10 ** 3                               # The maximum order of magnitude to which to calculate

buffer = []
values = []

now = datetime.now()

def log(text):
    with open(LOGFILE, 'a') as file:
        file.write(text + "\n")
        file.close()

# Main

def main():
    log(f" # Started LOG at {now.strftime('%d/%m/%Y %H:%M:%S')}")
    log(f" * POWER -> {POWER}\n * MAX_MAGNITUDE -> {MAX_MAGNITUDE}")
    for i in range(1, MAX_MAGNITUDE):
        for j in range(1, MAX_MAGNITUDE):
            r = (i ** POWER) + (j ** POWER)
            n = [i, j, r]
            if r in values:
                continue
            for k in buffer:
                if k[2] == r:
                    if n[0] != k[1] and n[1] != k[0]:
                        print(f" * found value -> {r}\n ({n[0]}, {n[1]})\n ({k[0]}, {k[1]})")
                        values.append(r)
                        log(f"{r} > ({n[0]}, {n[1]}) ({k[0]}, {k[1]})")

            buffer.append(n)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        end = datetime.now()
        delta = (end - now)
        print(f"\n * FINISHING computation at {end.strftime('%d/%m/%Y %H:%M:%S')}\n * working time -> {round(delta.total_seconds(), 2)} seconds")
        log(f" # FINISHING computation\n * FOUND total values -> {len(values)}\n * END time -> {end.strftime('%d/%m/%Y %H:%M:%S')}\n * working time -> {delta.total_seconds()} seconds\n\n")
        print("exiting...")
        exit(0)


