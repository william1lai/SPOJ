while True:
    n = input()
    if n == 0:
        break
    ans = 1
    for i in range(2, n+1):
        ans = ans + i*i
    print ans
