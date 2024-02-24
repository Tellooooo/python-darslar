N = int(input("N = "))
S = 0
for i in range( 1 , N ):
    if N % i == 0:
        S = S + i
        print("i = ", i)
if S == N:
    print("Mukammal son")
else:
    print("Mukammal son emas")
    