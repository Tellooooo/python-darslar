import math

a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))

d = b ** 2 - 4 * a * c

if a == 0:
    print("bu chiziqli tenglama")
elif d < 0:
    print("yechimga ega emas")
elif d == 0:
    x = ( -b ) / 2 * a
    print("x =", x)
else:
    x1 = (( -b ) + ( math.sqrt( d ))) * ( 2 * a )
    x2=(( -b ) - ( math.sqrt( d ))) * ( 2 * a )
    print( x1 , x2 )