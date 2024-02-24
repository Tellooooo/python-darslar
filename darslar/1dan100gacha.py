import random



A = []
B = []
for i in range(1 , 21):
    z = random.randint(1 , 100)
    A.append(z)
    
if 20 in A:
    print(A , "20 soni bor")
else:
    print(A , "20 soni yoq")    