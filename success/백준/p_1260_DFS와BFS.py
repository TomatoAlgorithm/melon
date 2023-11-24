"""
1. 문제 접근 방식 : 기본적인 dfs, bfs 구현으로 문제를 풀었음
2. 시간 복잡도 : O(N+M)
"""

from collections import deque, defaultdict

global graph, N
N, M, V = map(int, input().split(' '))
graph = defaultdict(list)

for _ in range(M):
    src, dst = map(int, input().split(' '))
    graph[src].append(dst)
    graph[dst].append(src)

for key in graph.keys():
    graph[key].sort()
    
def dfs(V, course, visited):
    global graph
    for dst in graph[V]:
        if not visited[dst]:
            visited[dst] = True
            course.append(dst)
            dfs(dst, course, visited)

def bfs(V):
    global graph, N
    visited = [False for _ in range(N+1)]
    visited[V] = True
    course = []
    que = deque()
    que.append(V)
    
    while len(que) > 0 :
        src = que.popleft()
        course.append(src)
        
        for dst in graph[src]:
            if not visited[dst]:
                que.append(dst)
                visited[dst] = True
                
    return course

#Main
visited = [False for _ in range(N+1)]

visited[V] = True
dfsCourse = [V]
dfs(V, dfsCourse, visited)
print(*dfsCourse, sep=' ')

bfsCourse = bfs(V)
print(*bfsCourse, sep=' ')