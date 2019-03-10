import math
import sys

n = int(sys.argv[1])
with open("hightemp.txt") as f:
    lines = f.readlines()

count = len(lines)
unit = math.ceil(count / n)

for i in range(n):
    with open("file" + str(i + 1) + ".txt", "w") as f:
        f.write("".join(lines[i * unit : (i + 1) * unit]))
