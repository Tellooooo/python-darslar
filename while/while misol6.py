N = int(input("N = "))
i = 1
S = 0
while i <= N:
    if N % i == 0:
        S += 1
    i += 1
if S == 2:
    print("tub son")
else:
    print("tub son emas")