x = int(input('x ='))
y = int(input('y ='))
z = int(input('z ='))

# KATTASINI CHIQARISH

if x > y > z:
    print('x katta')
elif x > z:
    print('x katta')
elif y > z:
    print('y katta')
else:
    print('z katta')

# KICHIGINI CHIQARISH

if x < y < z:
    print('x kichik')
elif x < z:
    print('x kichik')
elif y < z:
    print('y kichik')
else:
    print('z kichik')