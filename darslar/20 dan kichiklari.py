import random



A = []
B = []
for i in range(1 , 21):
    z = random.randint(1 , 100)
    A.append(z)

for i in A:
    if i <= 20:
        B.append(i)
print(B)