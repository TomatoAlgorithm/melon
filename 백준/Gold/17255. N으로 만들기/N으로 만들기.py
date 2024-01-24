given = input()
n = len(given)
if n == 1:
    print(1)
    exit()

answer = set()
sum = [0]
for _ in range(n):
    sum[0] = sum[0] * 2 + 1
def dfs(left, right, cur):
    global cnt, answer
    if len(cur) == sum[0]:
        answer.add(cur)
        return
    
    if left > 0:
        next_word = cur + given[left-1] + cur

        dfs(left-1, right, next_word)
    if right < n-1:
        next_word = cur + cur + given[right+1]

        dfs(left, right+1, next_word)


for i in range(n):
    dfs(i,i,given[i])

print(len(answer))