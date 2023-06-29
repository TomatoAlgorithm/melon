import sys

def input():
    return sys.stdin.readline().rstrip()

s = input().split(' ')
n = int(s[0])
k = int(s[1])

live = [True] * n

res = '<'
idx = 0

for index, isLive in enumerate(live, 0):
    
    if(isLive == True):


for i in range(1,n+1):
    cnt = 0
    tmp = idx
    while(True):
        if(tmp >= n):
            tmp %= n
        if(live[tmp] == True):
            cnt +=1
            if(cnt == k):
                live[tmp] = False
                res += str(tmp+1)
                idx = tmp
                break
        tmp += 1

    if i != n:
        res += ', '
res+='>'

print(res)