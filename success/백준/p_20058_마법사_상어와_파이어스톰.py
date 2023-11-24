"""
1. 문제접근방식
- firestorm 함수 만들기
    1. rotate 함수
        rotate 로직은
        board를 2**(n-level)만큼 돌면서
        해당 범위 안에서 요소들을 90도 시계회전 시키는 함수

    2. melting 함수
        그냥 4 방향 보면서 얼음 갯수가 3미만일 때는 녹이면 됨

2. 시간복잡도
    board 최대 = 64 * 64
    sum 최대 = 64 * 64
    bfs 최대 = 64 * 64
    Q 최대 1000 반복:
        rotate 최대 = 64 * 64
        melting 최대 = 64 * 64
        melting 복사 = 64 * 64

    3 * 1000 * (64 * 64) + 3 * (64 * 64) = 2003 * (64 * 64) = 12,300,288 => 가능
    
"""
from collections import deque

N, Q = map(int, input().split(' '))
tot = 2**N
board =[list(map(int, input().split(' '))) for _ in range(tot)]
levels = list(map(int, input().split(' ')))
# 시계방향 r b l t
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def firestorm(level):
    def rotate(level):
        for z in range(level, 0, -1): # 전체 블록 회전
            largeScale = 2**(N-z) # 전체 돌아야 하는 횟수
            smallScale = 2**(z - 1) # 그 안에서 움직여야 하는 범위
            for i in range(largeScale):
                for j in range(largeScale):
                    cur = [i * 2**(z), j * 2**(z)]
                    tmp = [row[cur[1] : cur[1] + smallScale] for row in board[cur[0] : cur[0] + smallScale]] # 그 안의 범위 안에 첫번째 꺼
                    save = [[0 for _ in range(smallScale)] for _ in range(smallScale)] 
                    for k in range(4):
                        cur[0] += dr[k] * smallScale
                        cur[1] += dc[k] * smallScale
                        for y in range(smallScale):
                            for x in range(smallScale):
                                nr = cur[0] + y
                                nx = cur[1] + x
                                save[y][x] = board[nr][nx]
                                board[nr][nx] = tmp[y][x]
                                tmp[y][x] = save[y][x]

    def melt():
        originBoard = [element[:] for element in board[:]]
        for i in range(tot):
            for j in range(tot):
                if originBoard[i][j] > 0 :
                    cnt = 0
                    for k in range(4):
                        nr = i+dr[k]
                        nc = j+dc[k]
                        if 0 <= nr < tot and 0 <= nc < tot and originBoard[nr][nc] > 0:
                            cnt += 1
                    if cnt < 3:
                        board[i][j] -= 1
    
    if level > 0:
        rotate(level)
    melt()

for level in levels:
    firestorm(level)

res = 0
for b in board:
    res += sum(b)

print(res)

덩어리 = 0
visited = [[False for _ in range(tot)] for _ in range(tot)]
for i in range(tot):
    for j in range(tot):
        if board[i][j] > 0 and visited[i][j] == False:
            que = deque()
            que.append((i,j))
            visited[i][j] = True
            cnt = 0
            while len(que) > 0:
                row, col = que.popleft()
                cnt += 1

                for k in range(4):
                    nr = row + dr[k]
                    nc = col + dc[k]

                    if 0 <= nr < tot and 0 <= nc < tot and board[nr][nc] > 0 and not visited[nr][nc]:
                        que.append((nr,nc))
                        visited[nr][nc] = True
            덩어리 = max(덩어리, cnt)

print(덩어리)