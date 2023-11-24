"""
1. 문제접근방식
    최초 풀이
    1. DSLR 정의
    D : 2*n % 10000
    S : n-=1 if n != 0 else n = 9999
    L : 
    strNum = ''
    for i in len(str(n)):
        if i != len(str(n)) - 1:
            strNum += str(n)[i+1]
        else:
            strNum += str(n)[0]
    n = int(strNum)
    R :
    strNum = str(n)[-1]
    for i in len(str(n)-1):
        strNum += str(n)[i]
    n = int(strNum)
    2. DSLR 로 BFS 진행

    => 무지성으로 진행 후 메모리 초과 발생
    => 여기서 답을 봣음,,
    => visited 사용
    => 이후 시간초과
    => 수학 적용(L, R)

2. 시간복잡도
    최악의 경우 => 10,000
"""
from collections import deque

T = int(input())

for _ in range(T):
    A, B = map(int, input().split(' '))

    visited = [False] * 10000

    que = deque()
    que.append((A, ''))
    visited[A] = True

    while True:
        cur, course = que.popleft()
        
        if cur == B:
            print(course)
            break

        for i in range(4):
            newCourse = course
            res = 0
            if i == 0:
                newCourse += 'D'
                res = (cur * 2) % 10000

            elif i == 1:
                newCourse += 'S'
                res = cur - 1 if cur != 0 else 9999

            elif i == 2:
                newCourse += 'L'
                res = (cur % 1000) * 10 + cur // 1000
                    
            elif i == 3:
                newCourse += 'R'
                res = cur // 10 + (cur % 10) * 1000

            if not visited[res]:
                visited[res] = True
                que.append((res, newCourse))
        