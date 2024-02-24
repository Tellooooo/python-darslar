def sum(*items):
    a = 0
    for item in items:
        a += item
    return a    
print(sum(4, 8, 3, 6, 2))