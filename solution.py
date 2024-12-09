import numpy as np

with open('2024-08-Suprise.txt') as f:
    lines = f.read().splitlines()
    intlines = np.array([int(i) for i in lines])

print("Solution is:", "".join(chr(i) for i in intlines if np.count_nonzero(intlines == i) <= 13))
