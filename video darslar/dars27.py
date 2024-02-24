def decor(func):
    def wrapper(*args, **kwards):
        print("Start")
        val = func(*args, **kwards)
        print("end")
        return val

    return wrapper

@decor
def p(x):
    # print(x*x)
    return x*x

a = p(5)

print(a)