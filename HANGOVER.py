arr = [0]
pikachu = 0.0
cards = 2
while pikachu < 5.20:
    pikachu = pikachu + 1.0/cards
    arr.append(pikachu)
    cards = cards + 1
arr.append(pikachu)

while True:
    n = input()
    if n == 0.00:
        break
    for i in range(len(arr)):
        if arr[i] >= n:
            print i, "card(s)"
            break
