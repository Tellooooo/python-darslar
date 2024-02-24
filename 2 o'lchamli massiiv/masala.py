# N = int(input("N = "))
# S = 0
# for i in range(1 , N + 1):
#     A = []
#     for j in range(1 , i + 1):
#         S = S + 1
#         A.append(S)
#     print(A)





# while True:
#     N = int(input("Kunni yozing ="))
#     A = {
#         1:"Dushanba" , 
#         2:"Seshanba" , 
#         3:"Chorshanba" , 
#         4:"Payshanba" , 
#         5:"Juma" , 
#         6:"Shanba" ,
#         7:"Yakshanba"
# }
#     if N in A:
#         print(A[N])
#     else:
#         print("bunday hafta kuni yoq")



N = int(input("Son = "))
A = {
    1: "bir xonalik",
    2: "ikki xonalik",
    3: "uch xonalik",
    4: "to'rt xonalik",
    5: "besh xonalik"
}
if len(str(N)) in A:
    print(A[len(str(N))])









