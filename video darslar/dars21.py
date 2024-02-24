def sum(*items):
    if len(items) == 0:
        return 0
    items2 = list(items)
    del items2[0]
    return items[0] + sum(*items2)

# x = sum(1, 15, 6, 8)

# print(x)