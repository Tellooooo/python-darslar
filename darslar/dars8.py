import math

X = int(input('X='))

# Y = ((X**2) + (X**4)) / ((X**4) + 1)

A = math.pow(X,2)

B = math.pow(A,2)

C = A + B

D = B + 1

Y = C / D

print('Y=', Y)