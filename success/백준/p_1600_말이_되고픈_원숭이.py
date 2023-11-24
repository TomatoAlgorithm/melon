"""
1. 문제접근방식
    말 처럼 뛸 수 있는 방향 8칸
    인접한 방향 4칸
    총 12칸으로 움직일 수 있는 부분인지 체크 후 움직이면 되지 않을까
    bfs 로 풀면 최단 경로가 나오지 않겠나
    근데 또 생각해보면 visited를 그냥 쓰면 K가 남아있을 때랑 아닐 때 방문이 다르다는 걸 체크하지 못함
    그래서 뛴 횟수가 많은지 체크하는 int 배열로 가는게 맞다

2. 시간복잡도
    최악의 경우 => W * H * 12 * 횟수 체크(이 경우의 최악의 수를 모르겠어용) = 40000 * 12 * 횟수 체크(이 경우의 최악의 수를 모르겠어용)
"""
from collections import deque

K = int(input())

W, H = map(int, input().split(' '))

board = [list(map(int, input().split(' '))) for _ in range(H)]
# visited = [[False for _ in range(W)] for _ in range(H)]
cntJump = [[-1 for _ in range(W)] for _ in range(H)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

hr = [-2,-2,-1,-1,1,1,2,2]
hc = [-1,1,-2,2,-2,2,-1,1]

def isOk(row, col, canJump):
    if 0 <= row < H and 0 <= col < W and board[row][col] == 0 and cntJump[row][col] < canJump:
        return True
    return False

que = deque()
que.append((0,0,0,K))
cntJump[0][0] = 0

while len(que) > 0:
    row, col, cnt, canJump = que.popleft()

    if row == H-1 and col == W-1:
        print(cnt)
        break
    
    if canJump > 0:
        for i in range(8):
            nr = row + hr[i]
            nc = col + hc[i]
            if isOk(nr, nc, canJump - 1):
                cntJump[nr][nc] = canJump - 1
                que.append((nr, nc, cnt+1, canJump-1))

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if isOk(nr, nc, canJump):
            cntJump[nr][nc] = canJump
            que.append((nr, nc, cnt+1, canJump))
else:
    print(-1)