n = input()
total = 0
i = 1
while True:
    if n < i*i:
        break
    total = total + ((n - i*i) / i) + 1
    i = i + 1
print total
        
