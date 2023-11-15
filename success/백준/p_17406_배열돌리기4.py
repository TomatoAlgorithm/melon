# 1. 문제 접근 방식 
# => 처음에는 회전 방식을 [r-i, s-i] => [r+i, s+i] 까지 전체 다 돌면서 값을 회전시키려고했는데
# 공책에 쓰다보니 방향만 잡으면 회전값들만 바꿀 수 있는걸 알았음
# 전체 다 도는 것보다 코드도 깔끔해지고 좋더라 
# 2. 시간 복잡도 => N * M * 6!(완탐)
# 3. 질문 사항
# 4. 그 외에 나누고 싶은 것들
# => board copy시에 그냥 copy를 해서 계속 틀렸었음
# deepcopy를 해서 문제해결은 하였음
# 근데 자료를 찾아보니 deepcopy보다 slicing이 더 빠르더라

global answer
answer = 1e9

N, M, K = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(N)]
rotate = [list(map(int, input().split(' '))) for _ in range(K)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def doRotate(board, n):
    # 회전 순서
    # r, c 재정의(배열에 맞게 1씩 뺀다)
    # 1. s만큼 돈다
    # 2. 4방향을 순회한다.(r - b - l - t)
    # 3. 방향마다 i*2 번 만큼 돌며 값을 돌린다.
    newBoard = [element[:] for element in board]
    [r, c, s] = rotate[n]
    
    r -= 1
    c -= 1
    
    for i in range(1,s+1):
        ny, nx = r-i, c-i
        tmp = newBoard[ny][nx]
        for j in range(4):
            for _ in range(i*2):
                nx += dx[j]
                ny += dy[j]
                save = newBoard[ny][nx]
                newBoard[ny][nx] = tmp
                tmp = save
    
    return newBoard

def dfs(depth, board, visited):
    global answer
    if depth == K:
        arrValue = 1e9
        for i in range(len(board)):
            arrValue = min(arrValue, sum(board[i]))
        answer = min(arrValue, answer)
        
    else:
        for i in range(len(visited)):
            if not visited[i]:
                newVisited = list(visited)
                newVisited[i] = True
                newBoard = doRotate(board, i)
                dfs(depth + 1, newBoard, newVisited)

dfs(0, board, [False for _ in range(K)])
print(answer)