"""
오른쪽 위로 가며 얻을 수 있는 최대 합
왼쪽 위로 가며 얻을 수 있는 최대 합
두 개 더하기
"""
N, M = map(int, input().split(' '))
scores = [list(map(int, input().split(' '))) for _ in range(N)]

up_scores = [([0]*M) for _ in range(N)]
down_scores = [([0]*M) for _ in range(N)]

up_scores[N-1][0] = scores[N-1][0]
down_scores[N-1][M-1] = scores[N-1][M-1]

for i in range(N-2,-1,-1):
    up_scores[i][0] = up_scores[i+1][0]+scores[i][0]
    down_scores[i][M-1] = down_scores[i+1][M-1]+scores[i][M-1]
for i in range(1,M):
    up_scores[N-1][i] = up_scores[N-1][i-1]+scores[N-1][i]
for i in range(M-2,-1,-1):
    down_scores[N-1][i] = down_scores[N-1][i+1]+scores[N-1][i]    

#up_dp
for i in range(N-2,-1,-1):
    for j in range(1,M):
        up_scores[i][j] = max(up_scores[i+1][j], up_scores[i][j-1]) + scores[i][j]

#down_dp
for i in range(N-2,-1,-1):
    for j in range(M-2,-1,-1):
        down_scores[i][j] = max(down_scores[i+1][j], down_scores[i][j+1]) + scores[i][j]

max_score = -1e9
for i in range(N):
    for j in range(M):
        max_score = max(max_score, up_scores[i][j] + down_scores[i][j])
        
print(max_score)