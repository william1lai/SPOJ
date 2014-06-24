ncases = input()
for i in range(ncases):
    n = input()
    men = sorted([int(x) for x in raw_input().split(' ')])
    women = sorted([int(x) for x in raw_input().split(' ')])
    total = 0
    for j in range(n):
        total = total + men[j]*women[j]
    print total
    
