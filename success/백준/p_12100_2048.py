"""
첫 제출 : 풀긴 풀었지만 코드가 너무 더러워서 리팩토링이 필요할 것 같음,,,
1차 수정 : 어차피 모든 배열이 각 방향으로 합쳐질 때 Row or Column 한 줄만 필요하기 때문에 이를 합치는 함수를 제작해서 Refactoring 진행

문제 접근 방식 :
    1. 방향마다 루프를 돌아야되는 순서를 정한다.
        L => Row - Col / 0, N
        R => Row - Col / N, 0
        T => Col - Row / 0, N
        B => Col - Row / N, 0
    
    2. loop는 cur가 벽을 만날 때(board의 끝까지)까지 돈다
    3. cur가 숫자일 때 다음 숫자까지 탐색한다.
    4-1. 
        if 다음에 만난 수가 동일한 숫자 라면:
            cur에 *2를 해주고 다음에 만난 숫자를 0으로 만들고 cur를 1증가시킨다
    4-2.
        else:
            cur = k
    5. cur에서 부터 반댓방향으로 탐색을 진행하고 가장 앞쪽 0을 찾아 해당 위치에 값을 위치시키고 2부터 반복.

시간 복잡도:
    모든 방향으로 최대 5번까지 움직일 수 있기 때문에 4^5
    1번 움직일 때마다 N*N 을 탐색하므로 N^2
    움직이는 과정에서 제일 앞으로 옮기는 작업 N(N+1)/2 * N

    (N^2 + N(N+1)/2 * N) * 4^5 = 4,710,400
"""

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

answer = -1

def move(board, d):
    newBoard = [element[:] for element in board]

    def merge(arr):
        nums = [n for n in arr if n != 0]
        merged = []
        i=0
        while i < len(nums):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                merged.append(nums[i] *2)
                i+=2
            else:
                merged.append(nums[i])
                i+=1
        
        return merged + [0] * (N-len(merged))


    if d == 0: #L
        for i in range(N):
            newBoard[i] = merge(newBoard[i])
    elif d == 1: #R
        for i in range(N):
            newBoard[i] = merge(newBoard[i][::-1])[::-1]
    elif d == 2: #T
        for i in range(N):
            res = merge([newBoard[k][i] for k in range(N)])
            for k in range(N):
                newBoard[k][i] = res[k]
    elif d == 3:# B
        for i in range(N):
            column = [newBoard[k][i] for k in range(N)]
            res = merge(column[::-1])[::-1]
            for k in range(N):
                newBoard[k][i] = res[k]

    return newBoard
    

def dfs(depth, board):
    global answer
    if depth == 5:
        for row in board:
            answer = max(answer, max(row))
        return
    
    for i in range(4):
        newBoard = move(board, i)
        dfs(depth + 1, newBoard)
    

dfs(0, board)
print(answer)