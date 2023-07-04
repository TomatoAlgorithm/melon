import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    tops = input().split(' ')
    tops = list(map(int, tops))
    topstack = []
    receive = [0] * n

    for i in range(len(tops)-1,-1, -1) :
        height = tops[i]
        
        cnt = 0

        for t in range(len(topstack)-1,-1,-1):
            if(topstack[t][1] >  height):
                break
            else:
                cnt+=1
        
        for c in range(cnt):
            top = topstack.pop()
            receive[top[0]] = i+1
        
        topstack.append((i,height))


    
    print(*receive,sep=' ')

solution()

