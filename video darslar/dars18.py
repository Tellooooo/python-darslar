import re                             #regex101.com

a = "My 15 first 2 Regular 3 Expression"

# MATN ICHIDAN SO'ZNI TOPISH
# b = re.search("first2", a)
# if b:
#     print(b)
# else:
#     print("none")

# MATN ICHIDAN TOPILGAN SO'ZNI LISTGA AYLANTIRISH
# b = re.findall('first', a)
# if b:
#     print(b)
# else:
#     print('none') 

# MATN ICHIDAN RAQAMLARNI AJRATIB LISTGA AYLANTIRISH
# b = re.findall("[0-9]+",a)
# print(b)

# MATNDAGI RAQAMLARNI SO'ZGA AYLANTIRISH
b = re.sub('[0-9]+','raqam', a)
print(b)
