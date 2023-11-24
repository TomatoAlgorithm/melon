"""
1. 문제 접근 방식
    - 단지에 속해 있다는 걸 어떻게 찾을 수 있을까?
    1. for 문을 돌면서 1을 만나면 4방향 bfs 탐색
    2. 4 방향 중 1이 있는지 체크 
    3. 있다면 visited True후 count 증가 que에 삽입
    4. 모든 인접한 1을 다 찾으면 count 저장 후 다음 1을 찾아 진행(이 때 visited 확인하면서 진행)
2. 시간복잡도
    - 모든 칸에 대해서 4방향 탐색이 이루어 질 수 있기 때문에 4N
"""
import sys
from collections import deque

N = int(input())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]

def searchNeighbor(row, col):
    que = deque()
    que.append((row, col))
    visited[row][col] = True
    cnt = 0
    
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    while len(que) > 0:
        [curRow, curCol] = que.popleft()
        cnt += 1

        for i in range(4):
            nr = curRow + dr[i]
            nc = curCol + dc[i]

            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 1 and not visited[nr][nc]:
                que.append((nr, nc))
                visited[nr][nc] = True
    
    return cnt

cntList = []

for row in range(N):
    for col in range(N):
        if board[row][col] == 1 and not visited[row][col]:
            cntList.append(searchNeighbor(row, col))

cntList.sort()
print(len(cntList))
print(*cntList, sep='\n')