N = 103
a = (N - 2) + 1 / N
for i in range(N - 2 , 0 , -2):
    a = i - 2 + 1 / a
print("a = " , 1 / a)