N = int(input())

friends = [([N] * (N+1)) for _ in range(N+1)]
for i in range(1,N+1):
    friends[i][i] = 0

while True:
    a, b = map(int, input().split(' '))
    if a == -1 and b == -1:
        break

    friends[a][b] = 1
    friends[b][a] = 1

for mid in range(1,N+1):
    for stt in range(1,N+1):
        for end in range(1,N+1):
            friends[stt][end] = min(friends[stt][end], friends[stt][mid] + friends[mid][end])

res = [a[1:] for a in friends[1:]]
answer = [(1e9, 1e9)]
for i in range(N):
    answer.append((max(res[i]), i+1))

answer.sort()
first = answer[0][0]
cnt = 0
for i in range(0,N):
    if answer[i][0] != first:
        break
    cnt += 1
print('{0} {1}'.format(first, cnt))
ceo = [a[1] for a in answer[:cnt]]
print(*ceo)