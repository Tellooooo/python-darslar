A = [ 6 , 7 , "abs" , 961 , 1 , 71 , ["abs"]]
kattasi = A[0]
a = 1
for i in A:
    a = a + 1
    if a % 2 != 0:
        if kattasi < i:
            kattasi = i  
print(A)
print(kattasi)