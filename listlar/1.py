x = int(input("x = "))
y = int(input("y = "))
if x % 2 == 0:
    if y % 2 == 0:
        print("qora")
if x % 2 == 0:
    if y % 2 != 0:
        print("oq")
if x % 2 != 0:
    if y % 2 != 0:
        print("qora")
if x % 2 != 0:
    if y % 2 == 0:
        print("oq")
        
