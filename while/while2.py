N = int(input(' N = '))
S = 0
S1 = 0
S2 = 0
i = 1
i1 = 1
i2 = 2

toq = int(input('toq sonlar = '))
juft = int(input(' juft sonlar = '))
hammasi = int(input(' hamma sonlar = '))


while i <= N:

    S = S + i
    # print(S)

    if not(i % 2):
        S1 = S1 + i1
        i1 = i1 + 2
        # print('S1',S1, ' i1',i1)

    else:
        S2 = S2 + i2
        i2 = i2 + 2
        # print('S2',S2, ' i2',i2)

    i = i + 1 

if (toq == 0) or (juft == 1) or (hammasi == 2) :
    print('toq sonlar = ', S1)
elif :
    print('juft sonlar = ', S2)
elif :
    print('hamma sonlar = ', S)
else:
    print('Xatolik !!!')