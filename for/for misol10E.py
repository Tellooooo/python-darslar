from math import *



N = int(input("N = "))

P = sqrt(N * 3)

for i in range(N - 1 , 0 , -1):

    P = sqrt(P + (3 * i))

print("P = ", P)


