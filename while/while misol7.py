N = int(input('N='))
i = 1
S = 1
A = 1
while N > A:
   while i < A :
      if A % i == 0 :
         S += 1
      i += 1
   if S == 0:
      print(i)
   A = A + 1
   i = 2
   S = 0