x = float(input("x="))
y = float(input("y="))
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
d = min(x, y)
g = min(a, b, c)
if d >= g:
    if d == x:
        if y >= a or y >= b or y >= c:
            print("Sig'adi")
        elif d == y:
            if x >= a or x >= b or x >= c:
                
                print("Sig'adi")
else:
    print("Sig'maydi")