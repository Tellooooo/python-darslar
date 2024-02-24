a = {
    "company": "Axe",
    "CPU": 8,
    "RAM": "16GB",
    "year": 2020
}

# MALUMOTNI TAHRIRLASH
# a['year'] = 2022

# MALUMOT QOSHISH
a['storage'] = '516GB'

# MALUMOTNI OCHIRISH
# del a['year']

# MALUMOTNI QATOR KORINISHIDA CHIQARISH
# for item in a:
#     print(a[item])

# MALUMOTNI KEYLARINI CHIQARISH
# for key in a.keys():
#     print(key)

# MALUMOTNI VALUELARINI CHIQARISH
# for value in a.values():
#     print(value)

# BARCHA MALUMOTLARNI QATOR KORINISHIDA CHIQARISH
# for key, value in a.items():
#     print(key,value)

# QATORNI HISOBLASH
# print(len(a))

# MAVJUD BOLMAGAN KEYNI CHIQARISH
print(a.get('game', 'CS 1.6'))