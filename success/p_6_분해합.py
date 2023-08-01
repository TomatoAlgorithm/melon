import sys
def input():
    return sys.stdin.readline().rstrip()

def 분해합(n):
    strn = str(n)
    res = 0
    for i in range(len(strn)):
        res += int(strn[i])

    return res

n = input()
minVal = int(n) - len(n)*9
minVal = max(0,minVal) 
for i in range(minVal,int(n)):
    if(i + 분해합(i) == int(n)):
        print(i)
        break
else:
    print(0)
