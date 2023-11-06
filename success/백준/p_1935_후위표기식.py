import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    stack = []
    n = int(input())

    expression = input()

    for i in range(n):
        repChar = chr(65+i)
        repNum = input().split('\n')

        expression = expression.replace(repChar,repNum[0]+' ')

    expression = expression.replace('+','+ ')
    expression = expression.replace('*','* ')
    expression = expression.replace('-','- ')
    expression = expression.replace('/','/ ')

    exList = expression.split(' ')[:-1]

    for l in exList:
        if(l == '+'):
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            stack.append(op1 + op2)
        elif (l=='*'):
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            stack.append(op1 * op2)
        elif (l=='-'):
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            stack.append(op1 - op2)
        elif (l=='/'):
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            stack.append(op1 / op2)
        else:
            stack.append(float(l))

    return round(stack[0], 2)

print("{:.2f}".format(solution()))