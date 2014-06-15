ncases = input()
for i in range(ncases):
    num = input()
    fivefactorcount = 0
    while num > 0:
        fivefactorcount = fivefactorcount + num/5
        num = num/5
    print fivefactorcount
    
