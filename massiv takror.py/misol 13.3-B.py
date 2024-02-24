n = int(input("n = "))
u0 = 1
f0 = 0
f1 = 1
if n > 1:
        M = [1 , 1]
        for i in range(0 , n + 1):
            b = len(M)
            u = M[b - 2] + M[b - 1]
            M.append(u)
        print(M)