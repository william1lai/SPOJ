dp = {}

def compute(n):
    if n == 0:
        return 0
    if n in dp:
        return dp[n]
    else:
        temp = compute(n/2) + compute(n/3) + compute(n/4)
        if temp > n:
            dp[n] = temp
        else:
            dp[n] = n
        return dp[n]

import sys
for s in sys.stdin:
    if len(s) == 0:
        break
    num = int(s)
    print compute(num)
