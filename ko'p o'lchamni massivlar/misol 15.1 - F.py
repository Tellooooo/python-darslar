# N = int(input("N = "))
# f = 0
# for i in range(N):
#     a = []
#     for j in range(N , 0 , -1):
#         if i <= j - 1:
#             a.append(f + 1)
#         elif i == j + 1:
#             a.append(0)
#         else:
#             a.append(0)
#     f += 1
#     print(a)


# N = int(input("N = "))
N = 5
A = []
a = []
for i in range(N):
    a = []
    for j in range(N):
        a.append(0)
    A.append(a)
print(A)
s = 1
for i in A:
    a = N
    for j in range(len(i)):
        i[j] = s
        if i[j] >= a + 1:
            i[j] = 0
        a -= 1    
    s += 1
    print(i)