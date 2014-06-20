
isPrime = []
primes = []

LIM = 31623
for i in range(LIM / 2):
    isPrime.append(True)
for i in range(3, 178, 2):
    for j in range(i*i, LIM, 2*i):
        isPrime[j / 2] = False
for i in range(3, LIM, 2):
    if isPrime[i / 2] == True:
        primes.append(i)

ncases = input()
for i in range(ncases):
    if i != 0:
        print ''
    nums = [int(x) for x in raw_input().split(' ')]
    low = nums[0]
    high = nums[1]
    if low <= 2:
        low = 3
        if high >= 2:
            print 2
    elif low % 2 == 0:
        low = low + 1
    if high % 2 == 0:
        high = high - 1
    isPrime = []
    for j in range(low, high + 1, 2):
        isPrime.append(True)

    for j in primes:
        if j > high:
            break
        temp = (low / j) * j
        if temp % 2 == 0:
            temp = temp + j
        for k in range(temp, high + 1, 2*j):
            if k >= low and k != j:
                isPrime[(k - low) / 2] = False

    for j in range(low, high + 1, 2):
        if isPrime[(j - low) / 2]:
            print j
    
