import math

A = int(input('A='))

# Y = (((math.pow(A,2) + B)**2) / C) + 5

B = math.pow(A,2)

C = B + 4

D = math.pow(C,2)

E = D / 7

Y = E + 5


print('Y=', Y)