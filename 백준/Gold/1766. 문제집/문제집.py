from collections import deque
from heapq import heappop, heappush

"""
1. N개의 문제는 모두 풀어야 한다.
2. 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
3. 가능하면 쉬운 문제부터 풀어야 한다.
"""

N, M = map(int, input().split(' '))

parents = {}
for i in range(1, N+1):
    parents[i] = []

indegree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split(' '))
    parents[A].append(B)
    indegree[B] += 1

que = []

res = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heappush(que, i)

while que:
    cur = heappop(que)
    res.append(cur)

    for parent in parents[cur]:
        indegree[parent] -= 1
        if indegree[parent] == 0:
            heappush(que, parent)

print(*res)