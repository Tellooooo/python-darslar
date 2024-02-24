try:
    a = 5/0
except Exception:
    raise ZeroDivisionError("0ga bo'lish")
else:
    print("Xatolik mavjud emas")
finally:
    print("tugatish")