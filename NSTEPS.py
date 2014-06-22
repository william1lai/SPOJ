ncases = input()
for i in range(ncases):
    pikachu = [int(x) for x in raw_input().split(' ')]
    x = pikachu[0]
    y = pikachu[1]
    if x == y:
        if x % 2 == 0:
            print 2*x
        else:
            print 2*x - 1
    elif x == y + 2:
        if x % 2 == 0:
            print 2*x - 2
        else:
            print 2*x - 3
    else:
        print "No Number"
