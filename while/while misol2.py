N = int(input(' N = '))
i = 1
S = 0
while i <= N:

    if N % i == 0:
        S = S + i
        print(' i = ', i)
    i = i + 1

print(' S = ', S)