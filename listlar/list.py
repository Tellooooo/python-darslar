# RO'YXAT YARATIW

# thislist = ["apple", "banana", "cherry"]
# print(thislist)


# IKKINCHI ELEMENTNI CHIQARISH

# thislist = ["apple" , "banana" , "cherry"]
# print(thislist[1])


# OXIRGI ELEMENTNI CHIQARISH

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])


# 3 , 4 , 5 ELEMENTLARNI CHIQARISH

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])


# KIWI GACHA BO'LGAN ELEMENTLARNI CHIQARISH
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])


# GILOSDAN BOWLAB OXIRIGACHA ELEMENTLARNI CHIQARISH
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])


# BU ORANGE DAN BOWLAB MELON GACHA BOLGAN ELEMENTLARNI O'Z ICHIGA OLADI

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])


# RO'YXATDA OLMA BORLIGINI TEKWIRIW

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("Bu listda 'apple' elementi bor")
# print("Listda 'apple' elementi yoq")


# IKKINCHI ELEMENTNI O'ZGARTIRIW

# thislist = ["apple" , "banana" , "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)


# BANAN VA GILOS ELEMENTLARINI QORA SMARODINA VA TARVUZ ELEMENTLARIGA O'ZGARTIRIW

# thislist = ["apple" , "banana" , "cherry" , "orange" , "kiwi" , "mango"]
# thislist[1 : 3] = ["blackcurrant" , "watermelon"]
# print(thislist)


# IKKINCHI ELEMENTNI YANGI IKKITA ELEMENTGA O'ZGARTIRIW

# thislist = ["apple" , "banana" , "cherry"]
# thislist[1 : 2] = ["blackcurrant" , "watermelon"]
# print(thislist)


# UCHINCHI ELEMENT SIFATIDA TARVUZ NI QO'WIW

# thislist = ["apple" , "banana" , "cherry"]
# thislist.insert(2 , "watermelon")
# print(thislist)


# append() ELEMENTNI QO'WIW USULIDAN FOYDALANIW

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)


# ELEMENTNI IKKINCHI POZITSIYA SIFATIDA KIRITING

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)


# tropical GA ELEMENTLARNI QO'WIW thislist:

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# RO'YXAT ELEMENTLARINI RO'YXATGA QO'WIW

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# BANAN NI OLIB TAWLAW

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# BANAN NING BIRINCHI KO'RINIWINI OLIB TAWLAW

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)


# IKKINCHI ELEMENTNI OLIB TAWLAW

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)


# OXIRGI ELEMENTNI OLIB TAWLAW

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)


# BIRINCHI ELEMENTNI OLIB TAWLAW

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)


# TO'LIQ RO'YXATNI O'CHIRIW

# thislist = ["apple", "banana", "cherry"]
# del thislist


# RO'YXAT TARKIBINI TOZALAW

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# RO'YXATDAGI BARCHA ELEMENTLARNI BIRMA BIR CHOP ETIW

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)


# BARCHA ELEMENTLARNI INDEKS RAQAMIGA QARAB CHOP ETIW

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])


# while  BARCHA INDEKS RAQAMLARINI O'TISH UCHUN TSIKLDAN FOYDALANIB BARCHA ELEMENTLARNI CHOP ETIW

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1


# for  RO'YXATDAGI BARCHA ELEMENTLARNI CHOP ETIW U-N QISQA TSIKLI

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# FAQAT ICHIDA A HARFI BOLGAN ELEMENTLARNI CHIQARISH

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)


# A HARFI BOR ELEMENTLARNI CHIQARISHNING QISQA USULI

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# OLMA DAN BOWQA HAMMA ELEMENTNI CHIQARISH

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if x != "apple"]

# print(newlist)


# range()   ITERATSIYANI YARATIW UCHUN FUNKSIYADAN FOYDALANIW MUMKIN

# newlist = [x for x in range(10)]

# print(newlist)


# FAQAT 5 DAN KICHIK RAQAMLARNI QABUL QILIW

# newlist = [x for x in range(10) if x < 5]

# print(newlist)


# YANGI RO'YXATDAGI QIYMATLARNI KATTA HARF BILAN BELGILAW

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x.upper() for x in fruits]

# print(newlist)


# YANGI RO'YXATDAGI BARCHA QIYMATLARNI 'SALOM' GA O'RNATIW

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = ['hello' for x in fruits]

# print(newlist)


# BANAN O'RNIGA APELSINNI QO'WIW

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)


# RO'YXATLARNI ALIFBO TARTIBIGA TARTIBLAW

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)


# RO'YXATNI RAQAMLAR BO'YICHA TARTIBLAW

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)


# RO'YXATNI KAMAYIWIGA QARAB TARTIBLAW

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)


# RAQAMNI 50 GA YAQINLIGIGA QARAB RO'YXATNI TARTIBLAW

# def myfunc(n):
#     return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


# KATTA - KICHIK HARFLARGA QARAB TARTIBLAW KUTILMAGAN NATIJANI BERIWI MUMKIN

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)


# copy() USULI BILAN RO'YXATNING NUSXASINI YARATISH

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# IKKITA RO'YXATNI QO'SHISH

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# RO'YXATNI 1 GA QO'WIW

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#     list1.append(x)

# print(list1)


# extend()  RO'YXAT LIST1 NI OXIRIGA LIST2 NI QO'SHISH UCHUN 

# list1 = ["a" , "b" , "c"]
# list2 = [1 , 2 , 3]

# list1.extend(list2)
# print(list1)


# append()	LISTGA ELEMENT QO'SHISH

# clear()	LISTNI TOZALASH

# copy()	RO'YXATNI NUSXASINI YARATISH

# count()	LIST ICHIDAGI ELEMENTLARNI SANASH

# extend()	LIST1 NI OXIRIGA LIST2 NI QO'SHISH

# index()	

# insert()	XOXLAGAN INDEKSIMIZDA ELEMENT QO'SHISH

# pop()	    ELEMENTNI OLIB TASHLASH

# remove()	ELEMENTNI BIRINCHI KO'RINISHINI OLIB TASHLASH

# reverse()	ELEMENTNI OXIRIDAN BOSHLAB CHIQARISH

# sort()	ELEMENTLARNI SARALASH


