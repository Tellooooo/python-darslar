from math import *



N = int(input( " N = "))
i = 2
S = 1
P = 1
J = 2
while J <= N:
    while i <= J:
        S = S * i
        i += 1
    J += 1
    i = 1
    P = pow((1 + ( 1 / S)), 2) + P
    S = 1
if N == 1:
    print("shart xato")
else:
    print("P =", P)