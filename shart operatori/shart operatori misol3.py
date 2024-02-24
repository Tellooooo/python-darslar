from math import *

x = int(input('x ='))
y = int(input('y ='))
z = int(input('z ='))

# KATTASINI CHIQARISH

a = x + y + z
b = x * y * z

if a > b:
    print('a katta')
else:
    print('b katta')

# KICHIGINI CHIQARISH

A = (( x + y + z ) / 2 ) ** 2 + 1
B = ( x * y * z ) ** 2 + 1

if A > B:
    print('A kichik')
else:
    print('B kichik')