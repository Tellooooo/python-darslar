N = int(input(' N = '))
i = 2
S = 0
A = 2
while A <= N:

    while i < A:

        if A % i == 0:

            S = S + i

            if S == A:

                print(S)

        i = i + 1

    A = A + 1

    S = 0   

    i = 1


