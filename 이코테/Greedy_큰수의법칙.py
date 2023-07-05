import sys

def input():
    return sys.stdin.readline().rstrip()

def mySolution(l,m,k):
    max1 = max(l)
    l.remove(max1)
    max2 = max(l)

    res = 0
    cnt = 0
    for i in range(m):
        if(cnt == k):
            res += max2
            cnt = 0
            continue
        res+=max1
        cnt+=1
    
    print(res)

def CorrectAnswer(l,m,k):
    l.sort()
    first = l[-1]
    second = l[-2]

    res = 0

    count = m//(k+1) * k
    count += m%(k+1)

    res = 0
    res += count * first
    res += (m - count) * second
    
    print(res)


n,m,k = map(int,input().split(' '))
l = list(map(int,input().split(' ')))

CorrectAnswer(l,m,k)
mySolution(l,m,k)