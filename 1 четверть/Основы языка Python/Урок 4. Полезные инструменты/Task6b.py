from itertools import *


C = 0
for i in cycle('12345'):
    if C > 10:
        break
    C += 1
    print(i)
