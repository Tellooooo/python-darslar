from math import *



N = int(input("N = "))
S = 0
for c in range(1 , N + 1):
    C = pow(c , 2)
    for a in range(1 , c + 1):
        for b in range(1 , a + 1):
            D = pow (a , 2) + pow (b, 2)
            if C == D:
                print("Pifagor sonlar", b , a , c)
    C = 0