A = [ 1 , 2 , 3 , 1 , 6 , 8 , 5 , 9 , 0]
kattasi = A[0]
a = 1
for i in A:
    a = a + 1
    if a % 2 == 0:
        if kattasi < i:
            kattasi = i  
print(A)
print(kattasi)