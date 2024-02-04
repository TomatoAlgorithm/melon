N, K = map(int, input().split(' '))
children = list(map(int, input().split(' ')))
if K == 1:
    print(children[-1]-children[0])
    exit()
diff = [0] * (N-1)

for i in range(0,N-1):
    diff[i] = (children[i+1] - children[i], i)

diff.sort(reverse=True)
answer = 0


diff = diff[:K-1]
diff = [a[1] for a in diff]

diff.sort()

answer = children[diff[0]] - children[0]
for i in range(len(diff)):
    if i == len(diff)-1:
        answer += children[-1] - children[diff[i]+1]
    else:
        answer += children[diff[i+1]] - children[diff[i]+1]
print(answer)