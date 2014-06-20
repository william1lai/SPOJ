# let + = 0, - = 1, * = 2, / = 3, ^ = 4

def isOp(ch):
    return ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '^'

def opPrec(ch):
    if ch == '+':
        return 0
    elif ch == '-':
        return 1
    elif ch == '*':
        return 2
    elif ch == '/':
        return 3
    elif ch == '^':
        return 4
    else:
        return -1

ncases = input()
for i in range(ncases):
    line = raw_input()
    ans = ""
    operators = []

    for j in range(len(line)):
        if line[j] == '(':
            operators.append('(')
        elif line[j] == ')':
            top = operators.pop()
            while top != '(':
                ans = ans + top
                top = operators.pop()
        elif isOp(line[j]):
            if operators == []:
                operators.append(line[j])
            else:
                top = operators.pop()
                while operators != [] and top != '(' and opPrec(line[j]) <= opPrec(top):
                    ans = ans + top
                    top = operators.pop()
                if opPrec(line[j]) <= opPrec(top):
                    ans = ans + top
                else:
                    operators.append(top)
                operators.append(line[j])
        else:
            ans = ans + line[j]

    print ans
