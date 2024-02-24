N = int(input("N = "))
A = []
a = []
for i in range(N):
    a = []
    for j in range(N):
        a.append(0)
    A.append(a)
print(A)

for j in range(0 , N):
    for k in range(0 , N):
        if k == j:
            a[j] = 2
        elif k == j - 1:
            a[k] = 1
        elif k == j + 1:
            a[k] = 1
        a[j - 2] = 0
    print(a)







# qadam = 0
# for i in range(len(A)):
#     i[qadam] = 2
#     i[qadam + 1] = 1
#     if qadam != 0:
#         i[qadam - 1] = 1
#     i[qadam - 2] = 0

#     qadam += 1

#     print(i)

# for j in range(N):
#     A[j - 2] = 0
#     if j != 0:    
#         A[j - 1] = 1
#     if j == 0:
#         A[j + 1] = 1
#     A[j] = 2
#     print(A)