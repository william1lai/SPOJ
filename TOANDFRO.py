import sys

while True:
    n = input()
    if n == 0:
        break
    text = raw_input()
    rebuild = ""
    pikachu = len(text) / n
    for i in range(pikachu):
        if i % 2 == 0:
            rebuild = rebuild + text[i*n:(i+1)*n]
        else:
            rebuild = rebuild + text[i*n:(i+1)*n][::-1]
    for i in range(n):
        for j in range(i, len(rebuild), n):
            sys.stdout.write(rebuild[j])
    sys.stdout.write("\n");
