# 니니즈 대학에 입학한 학생들은 각각 고유한 학번(ID)을 1 부터 n 까지 부여 받습니다.
# 처음에는 학생들끼리 서로를 잘 알지 못하고 각각 다른 친구들이 있습니다.
# 학기가 진행됨에 따라 다른 친구 그룹이 무작위로 형성되기 시작 합니다. 

# 각각 색인으로 정렬된 세 개의 배열이 있습니다. 
# 첫 번째 배열에는 Friend 또는 Total 이 될 queryType 이 포함됩니다. 
# 다음 두 배열 students1 과 students2 에는 각각의 학생 학번(ID)이 포함 됩니다. 
# queryType 이 Friend 이면 두 학생은 같은 친구 그룹이 됩니다.
# queryType 이 Total 인 경우 각 학생이 속한 친구 그룹의 친구 수 합계를 보여 줍니다. 

# Example

# n = 4
# queryType = ['Friend', 'Friend', 'Total']
# students1 = [1, 2, 1]
# students2 = [2, 3, 4] 

def dfs(graph, n,visited):
    visited.append(n)

    for node in graph[n]:
        if node not in visited:
            dfs(graph, node, visited)
    
    return visited

def solution(n, queryType, students1, students2):
    graph = [[] for _ in range(n+1)]
    for idx, query in enumerate(queryType,0):
        if query == 'Friend':
            graph[students1[idx]].append(students2[idx])
            graph[students2[idx]].append(students1[idx])
        elif query == 'Total':
            visited = []
            res1 = len(dfs(graph, students1[idx], visited))
            visited = []
            res2 = len(dfs(graph, students2[idx], visited))
            return res1 + res2

n = 4
queryType = ['Friend', 'Friend', 'Total']
students1 = [1, 2, 1]
students2 = [2, 3, 4] 

print(solution(n,queryType,students1,students2))

