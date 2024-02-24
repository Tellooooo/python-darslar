N = int(input(' N = '))
i = 1 
while i <= N:
    if (i % 3 ==0) and not(i % 5 == 0):
        print('i = ', i)
    i += 1
