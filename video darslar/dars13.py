def sorting(s):
    return str(s)

a = [34,76,35]
b = ["Tillo","Miron","Timur"]
c = ["Tillo", 46,"Miron","Timur", 83]

# LISTNI TARTIB BILAN JOYLASHTIRISH
# a.sort()
# b.sort()
# c.sort( key = sorting)

# LISTNI CHAPPA TARTIBDA JOYLASHTIRISH
# a.sort(reverse=True)
# b.sort(reverse=True)
c.sort( key = sorting, reverse=True)

print(a)
print(b)
print(c)