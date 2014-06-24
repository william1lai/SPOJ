while True:
    n = input()
    if n == -1:
        break
    bags = []
    total = 0
    for i in range(n):
        temp = input()
        total = total + temp
        bags.append(temp)
    if (total / n)*n != total:
        print -1
    else:
        diff = 0
        avg = total / n
        for j in range(n):
            diff = diff + abs(avg - bags[j])
        print diff / 2
    
