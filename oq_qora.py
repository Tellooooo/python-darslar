N = int(input("N ="))
M = int(input("M ="))
if N % 2 == 0:
    if M % 2 == 0:
        print("oq")
if N % 2 != 0:
    if M % 2 != 0:
        print("oq")
if N % 2 != 0:
    if M % 2 == 0:
        print("qora")
if N % 2 == 0:
    if M % 2 != 0:
        print("qora")
if N > 4:
    print("seni chegarang")
else:
    print("meni chegaram")