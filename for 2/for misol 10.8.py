X = float(input("X = "))
N = 8
a = (X ** 2) + (2 ** N) / X ** 2
for i in range(1 , N):
    S = N - i
    a = (X ** 2) + (2 ** S) / a
print("a = " , 1 / a)