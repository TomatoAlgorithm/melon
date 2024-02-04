from collections import deque

N = int(input())
nums = list(map(int, input().split(' ')))
plus, minus, multi, div = map(int, input().split(' '))
ops = ['+','-','*','/']

global mav, miv
mav = 1e9 * -1
miv = 1e9

def calc(exp):
    exp = deque(exp)
    newnums = deque(nums)

    numstack = deque()
    expstack = deque()
    numstack.append(newnums.popleft())
    
    while exp:
        numstack.append(newnums.popleft())
        cur = exp.popleft()

        if cur == '+' or cur == '-':
            expstack.append(cur)
        elif cur == '*':
            num1 = numstack.pop()
            num2 = numstack.pop()
            res = num1 * num2
            numstack.append(res)
        elif cur == '/':
            num1 = numstack.pop()
            num2 = numstack.pop()
            res = num2 // num1
            numstack.append(res)
        

    while expstack:
        cur = expstack.popleft()
        num1 = numstack.popleft()
        num2 = numstack.popleft()
        res = 0

        if cur == '+':
            res = num1 + num2
        elif cur == '-':
            res = num1 - num2

        numstack.appendleft(res)

    return numstack[0]

def dfs(depth, remain, cur, dup, N):
    global mav, miv
    if depth == N:
        res = calc(cur)
        mav = max(mav, res)
        miv = min(miv, res)
        return
    
    for i in range(4):
        if remain[i] > 0:
            newCur = cur + ops[i]
            if newCur not in dup:
                newRemain = remain[:]
                newRemain[i] -= 1
                dup.add(newCur)
                dfs(depth + 1, newRemain, newCur, dup, N)
            

dup = set()
dfs(0, [plus, minus, multi, div], '', dup, plus+minus+multi+div)
print(mav)
print(miv)