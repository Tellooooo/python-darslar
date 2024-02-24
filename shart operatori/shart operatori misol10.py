from math import *

x = float(input('x='))
y = float(input('y='))

a=min(x, y) 
b=max(x, y)

z=(x+y)/2
u=pow(x*y, 2)


if a==x:
    x = z
    print('min=',x)
elif b==y:
    y = u
    print('max=', y)

