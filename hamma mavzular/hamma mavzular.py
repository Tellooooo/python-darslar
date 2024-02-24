from math import *
import random

class mavzu_9:
    def misol_1():
        N = int(input("N = "))
        for i in range( 1, N + 1 ):
            if N % i == 0:
                print("i = ", i)
    def misol_2():
        N = int(input("N = "))
        S = 0
        for i in range( 1 , N + 1 ):  
            if N % i == 0:
                S = S + i
        print("S = ", S)
    def misol_3():
        N = int(input("N = "))
        S = 0
        for i in range( 1 , N ):
            if N % i == 0:
                S = S + i
                print("i = ", i)
        if S == N:
            print("Mukammal son")
        else:
            print("Mukammal son emas")
    def misol_4():
        N = int(input("N = "))
        S = 0 
        for i in range(1 , N + 1):
            for J in range(1 , i):
                if i % J == 0:
                    S += J
            if S == i:
                print("S = ", S)
            S = 0
    def misol_5():
        N = int(input("N = "))
        for i in range( 1 , N + 1 ):
            if (i % 3 == 0) and not(i % 5 == 0):
                print("i = ", i)
    def misol_6():
        N = int(input("N = "))
        S = 0
        for i in range( 1 , N + 1):
            if N % i == 0:
                S += 1
        if S == 2:
            print("tub son")
        else:
            print("tub son emas")
    def misol_7():
        N = int(input("N = "))
        S = 0
        for i in range(1 , N):
            for J in range(1 , i + 1):
                if i % J == 0:
                    S += 1
            if S == 2:
                print( J)
            S = 0
    def misol_8():
        N = int(input("N = "))
        S = 0
        for c in range(1 , N + 1):
            C = pow(c , 2)
            for a in range(1 , c + 1):
                for b in range(1 , a + 1):
                    D = pow (a , 2) + pow (b, 2)
                    if C == D:
                        print("Pifagor sonlar", b , a , c)
            C = 0
    def misol_10_B():
        N = int(input(' N = '))
        S = 1
        for i in range(1 , N + 1):
            S = S * i
            print("S = ", S)
    def misol_10_D():
        N = int(input(' N = '))
        S = 0
        P = 1
        for i in range(1 , N + 1):
            S = (1 + (1 / pow(i , 2)))
            P = P * S
        print("P = ", P)
    def misol_10_E():
        N = int(input("N = "))

        P = sqrt(N * 3)

        for i in range(N - 1 , 0 , -1):

            P = sqrt(P + (3 * i))

        print("P = ", P)
    def misol_10_F():
        N = int(input("N = "))
        s = 0
        P = 0
        for i in range(1 , N + 1):
            for J in range(1 , i + 1):
                S = sin(N)
                s = S + S
            P = 1 / S
            s = 0
        print("P = ", P)
    def misol_10_G():
        N = int(input("N = "))
        s = 0
        P = 0
        g = 0
        for i in range(1 , N + 1):
            for J in range(1 , N + 1):
                S = sin(J)
                G = cos(J)
                s = S + s
                g = G + g
            P = (g / s) + P
            g = 0
            s = 0
        print("P = ", P)
    def misol_11_A():
        N = int(input("N = "))
        S = 0
        P = 0
        for i in range(1 , N + 1):
            S = 1 / pow(i , 2)
            P += S
        print("P = ", P)
    def misol_11_B():
        N = int(input("N = "))
        S = 0
        P = 0
        for i in range(1 , N + 1):
            S = 1 / pow(i , 3)
            P += S
        print("P = ", P)
    def misol_11_C():
        N = int(input("N = "))
        S = 0
        P = 1
        for J in range(1 , N + 1):
            for i in range(1 , J + 1):
                P = P * i
            S = ( 1 / P) + S
            P = 1
        print("P = ", P)
    def misol_11_D():
        N = int(input("P = "))
        S = 0
        for i in range(1 , N + 1):
            S = pow(1 / (2 * i) , 2) + S
        print("S = ", S)
    def misol_11_E():
        N = int(input("N = "))
        P = 1
        for i in range(2 , N + 1):
            P = ( i + 1) / (i + 2) * P
        print("P = ", P)
    def misol_11_F():
        N = int(input("N = "))
        P = 1
        S = 1
        for J in range(2 , N + 1):
            for i in range(2 , J + 1):
                S = S * i
            P = ((1 + (1 / S)) ** 2) * P
            S = 1
        print("P = ", P)
    def misol_12_B():
        A = float(input("A = "))
        N = int(input("N = "))
        S = 1
        for i in range(1 , N + 1):
            s = (A + i - 1)
            S = S * S
        print("S = ", S)
    def misol_12_C():
        A = float(input("A = "))
        N = int(input("N = "))
        S = 0
        s = 1
        for i in range(1 , N + 1):
            for J in range(1 , i + 1):
                M = (A - 1 + J)
                s = s * M
            S = S + (1 / s)
            s = 1
        print("S = ", S)
    def misol_12_D():
        A = float(input("A = "))
        N = int(input("N = "))
        S = 1
        for i in range(1 , N):
            s = (A - i * N)
            S = S * s
        print("S = ", S)
    def misol_13():
        N = int(input("N = "))
        S = 1
        A = 1
        for i in range(0.1 , N + 1 , 0.1):
            
            S = (A + (sin(i))) * S
            
        print("S = ", S)
    def misol_14():
        N = int(input("N = "))
        A = float(input("A = "))
        X = float(input("X= "))
        P = 1
        P = (X + A) ** 2
        for i in range(2 , N + 1):
            P = ((P + A) ** 2)
        print("P = ", P)
    def misol_15():
        N = int(input("N = "))
        S = 0
        P = 1
        for i in range(2 , N + 1):
            for J in range(i , (i * 2) + 1):
                P = P * J
            S = S + P
            P = 1
        print("S = ", S + 2)
        
