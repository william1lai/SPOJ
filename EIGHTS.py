nums = []
for i in range(192, 1000):
    if i*i*i % 1000 == 888:
        nums.append(i)
#192 442 692 942

ncases = input()
for i in range(ncases):
    n = input()
    a, b = ((n - 1) / 4)*1000, (n - 1) % 4
    print a + nums[b]
