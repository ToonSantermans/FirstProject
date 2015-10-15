from __future__ import print_function, division
import numpy as np
import sys

N = int(sys.argv[1])

print(" N is ", N)

for number in np.random.normal(size=N):
	print(number)

for line in sys.stdin:
	x = float(line)
