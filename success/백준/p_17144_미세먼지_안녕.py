# 1. 문제 접근 방식
# => 구현
# => 확산 방법
# => 1. 새로운 보드를 만든다
# => 2. 칸마다 진행하며 기존 보드의 값으로 확산한 값을 새로운 보드에 더해준다 
# => 순환 방법 => 각 시작인덱스에서 방향 별로 진행하면 될듯
# 2. 시간 복잡도 => T * ((R * C * 4)[확산] + (2 * 2 * (R + C))[순환]) 

R, C, T = map(int, input().strip().split(' '))

board = [list(map(int, input().strip().split(' '))) for _ in range(R)]
robotStart = -1 # 공기청정기 윗부분
robotEnd = -1 # 공기청정기 아랫부분

# r b l t (시계)
dr = [0,1,0,-1] 
dc = [1,0,-1,0]    

for i in range(2,R-2):
    if(board[i][0] == -1):
        robotStart = i
        robotEnd = i+1
        break

def spreadCheck(r,c):
    res = [False for _ in range(4)]
    
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        res[i] = 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1
    
    return res

def spread(board): #확산
    newBoard = [[0 for _ in range(C)] for _ in range(R)]
    newBoard[robotStart][0] = -1
    newBoard[robotEnd][0] = -1

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0 :
                can = spreadCheck(i,j) # 확산 가능한 방향
                value = board[i][j] // 5
                for k in range(len(can)):
                    if can[k]:
                        newBoard[i+dr[k]][j+dc[k]] += value
                        board[i][j] -= value
                newBoard[i][j] += board[i][j]

    return newBoard

def rotate(board, up): #공기 청정기
    start = robotStart if up == -1 else robotEnd
    columnRange = robotStart if up == -1 else R - (robotEnd + 1)
    tmp = 0
    nr = start
    nc = 0
    for i in range(4):
        if i % 2 == 0:
            for _ in range(C-1):
                nr += dr[i]
                nc += dc[i]
                save = board[nr][nc]
                board[nr][nc] = tmp
                tmp = save
        else:
            for _ in range(columnRange):
                nr += dr[i] * up
                nc += dc[i] * up
                save = board[nr][nc]
                board[nr][nc] = tmp
                tmp = save
    board[nr][nc] = -1

answer = 0
for _ in range(T):
    board = spread(board)
    rotate(board, -1)
    rotate(board, 1)

for b in board:
    answer += sum(b)

print(answer + 2)