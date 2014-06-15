def rev(num):
    temp = 0
    while num > 0:
        temp = temp*10 + num%10
        num = num / 10
    return temp

ncases = input()
for i in range(ncases):
    pair = [int(x) for x in raw_input().split(' ')]
    reva = rev(pair[0])
    revb = rev(pair[1])
    ans = rev(reva + revb)
    print ans
