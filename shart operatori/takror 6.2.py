X = int(input("X = "))
Y = int(input("Y = "))
Z = int(input("Z = "))
if X > Y and X > Z:
    print("X katta")
elif Y > X and Y > Z:
    print("Y katta")
elif Z > X and Z > Y:
    print("Z katta")
else:
    print("KIchik yoki teng")