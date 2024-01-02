N = int(input())

def dfs(depth, visited, word, cur, res, dup):
    if depth == len(word):
        res.append(cur)
        return
    
    for i in range(len(word)):
        if not visited[i]:
            newWord = cur + word[i]
            if newWord not in dup:
                dup.add(newWord)
                newVisit = visited[:]
                newVisit[i] = True
                dfs(depth+1, newVisit, word, newWord, res, dup)


for _ in range(N):
    res = []
    dup = set()

    word = list(input())
    word.sort()

    dfs(0, [False] * len(word), word, '', res, dup)

    res = list(res)
    res.sort()
    print(*res, sep='\n')