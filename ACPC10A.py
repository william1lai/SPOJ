while True:
    nums = [int(x) for x in raw_input().split(' ')]
    if nums[0] == 0 and nums[1] == 0 and nums[2] == 0:
        break
    if nums[1] - nums[0] == nums[2] - nums[1]:
        print "AP", (2*nums[2] - nums[1])
    else:
        print "GP", (nums[2]**2 / nums[1])
