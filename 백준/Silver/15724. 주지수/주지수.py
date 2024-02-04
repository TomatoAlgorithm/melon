import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

land = [(list(map(int, input().split(' ')))) for _ in range(N)]
mem = [([0]*M) for _ in range(N)]

mem[0][0] = land[0][0]
for i in range(1,M):
    mem[0][i] = mem[0][i-1] + land[0][i]
for i in range(1,N):
    mem[i][0] = mem[i-1][0] + land[i][0]

for i in range(1, N):
    for j in range(1, M):
        mem[i][j] = mem[i-1][j] + mem[i][j-1] - mem[i-1][j-1] + land[i][j]
        
T = int(input())

for _ in range(T):
    res = 0

    r1, c1, r2, c2 = map(lambda x: int(x)-1, input().split(' '))
    res = mem[r2][c2]
    flag = 0
    if r1 > 0:
        r1 -= 1
        res -= mem[r1][c2]
        flag += 1
    if c1 > 0:
        c1 -= 1
        res -= mem[r2][c1]
        flag += 1
    if flag == 2:
        res += mem[r1][c1]
    print(res)