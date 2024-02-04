N, M, K = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(N)]

answer = -1e5
stack = []

def dfs(row, col, depth, k, cur):
    global answer, stack
    if depth == k:
        answer = max(answer, cur)
        return
    
    for i in range(row, N):
        for j in range(col if i == row else 0, M):
            rc = [i,j]
            if rc not in stack and [i-1,j] not in stack and [i,j-1] not in stack:
                stack.append(rc)
                dfs(i,j,depth+1,k,cur+board[i][j])
                stack.pop()
dfs(0,0,0,K,0)
print(answer)