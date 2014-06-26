ncases = input()
for i in range(ncases):
    raw_input()
    n = input()
    total = 0
    for j in range(n):
        temp = input()
        total = total + temp
    if total % n == 0:
        print "YES"
    else:
        print "NO"
