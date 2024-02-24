a = int(input('a ='))
b = int(input('b ='))
c = int(input('c ='))
d = int(input('d ='))

if d >= c >= b >= a:
    print('javob =', 'a =' , d , 'b =' , d , 'c =' , d , 'd =', d)
elif a > b > c > d:
    print('javob =', 'a =',  a , 'b =' , b , 'c =' , c , 'd =' , d)
else:
    print('javob =', 'a =', a**2 , 'b =', b**2 , 'c =', c**2 ,'d =', d**2)