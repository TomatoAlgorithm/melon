from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split(' '))

    times = [0] + list(map(int, input().split(' ')))
    dp = [0] * (N+1)

    parents = {} # 부모 리스트
    childs = {} # 자식 리스트
    for i in range(1, N+1):
        parents[i] = []
        childs[i] = []
    indegree = [0] * (N+1) # 진입 차수 리스트

    for _ in range(K): # 진입 차수, 부모 리스트 초기화
        child, parent = map(int, input().split(' '))
        indegree[parent] += 1
        parents[child].append(parent)
        childs[parent].append(child)
    
    final = int(input())

    que = deque()

    for i in range(1, N+1): # 진입차수가 0 인 노드들은 큐에 삽입
        if indegree[i] == 0:
            que.append(i)
            dp[i] = times[i]

    """
    큐가 빌 때까지 반복
    부모 노드들의 진입차수를 줄이고,
    진입차수가 0이 된 노드들을 큐에 삽입한다.
    """
    while que:
        cur = que.popleft()

        for parent in parents[cur]:
            indegree[parent] -= 1
            if indegree[parent] == 0: # 진입 차수가 0 이 되었을 때 => 자식 노드들 중 시간 초를 비교하고 더 많이 걸리는 걸로 dp에 메모이제이션
                que.append(parent)
                res = 0
                for child in childs[parent]:
                    res = max(dp[child], res)
                dp[parent] = res + times[parent]
    print(dp[final])