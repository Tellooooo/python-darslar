A = [3 , 2 ,4 , 6, 7 , 6, 7 ,8]
S = 1
P = 0
for i in A:
    S = S * i
    B = len(A)
    P = S ** 1 / B
print(S)
print(P)