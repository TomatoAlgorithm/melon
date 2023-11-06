import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    cur = list(map(int,input()))
    target = list(map(int,input())) 

    res = turnCount(cur.copy(), target, n, 0)
    if res[0]:
        print(res[1])
        return
    cur[0] = 1 - cur[0]
    cur[1] = 1 - cur[1]
    res = turnCount(cur, target, n, 1)
    if(res[0]):
        print(res[1])
    else:
        print(-1)

def turnCount(lightList, targetList, n, cnt):
    for i in range(1,n):
        if i == n-1:
            if(lightList[i-1] != targetList[i-1]):
                cnt +=1
                lightList[i-1] = 1 - lightList[i-1]
                lightList[i] = 1 - lightList[i]
        else:
            if(lightList[i-1] != targetList[i-1]):
                cnt +=1
                lightList[i-1] = 1 - lightList[i-1]
                lightList[i] = 1 - lightList[i]
                lightList[i+1] = 1 - lightList[i+1]
    if lightList == targetList:
        return [True, cnt]
    else:
        return [False, -1]
    

main()