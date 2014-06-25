ncases = input()
for i in range(ncases):
    a,b = [int(x) for x in raw_input().split(' ')]
    if b == 0:
        print 1
    elif a % 10 == 0:
        print 0
    else:
        a = a % 10
        b = (b % 4) + 4
        print ((a % 10)**b) % 10
