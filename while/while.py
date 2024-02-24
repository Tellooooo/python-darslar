# i = 1
# S = 0
# while i <= 100:
#     S = i % 10 
#     print(S)
#     i += 1

# i = 1
# S = 0
# while i <= 100:
#     S = i // 10 
#     print(S)
#     i += 1

# i = 100
# S = 0
# while i >= 1:
#     S += i 
    
#     print(i)
#     i -= 1


# N = int(input(' N = '))
# i = 1
# A = 0
# B = 0
# # C = 0
# # D = 0
# # sum = 0

# while i <= N:
#     A = i // 100 
#     B = i // 10
#     C = B % 10
#     D = i % 10
#     sum = (D * 100) + (C * 10) + (A * 1)
#     i += 1

# print(sum)


from math import*
N = int(input("N ="))
i = 1
a = int(input("a ="))
while i <= N:
    print(pow(a,i))
    i+= 1