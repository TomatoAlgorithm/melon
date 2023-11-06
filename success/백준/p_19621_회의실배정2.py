import sys

def input():
    return sys.stdin.readline().rstrip()

    # 회의실 배정2 풀이법
    # 1. 강의가 끝나는 시간을 기준으로 오름차순 정렬을 한다
    # 2. 끝나는 시간이 같다면 강의시간이 더 짧은 순서로 정렬을 한다(시작과 동시에 끝나는 수업이 있기 때문에)
    # 3. 이렇게 정렬이 되면 강의가 끝나는 시간을 변수에 저장한다
    # 4. 그 다음 리스트를 순회하며 정렬된 강의들의 시작시간을 비교해서 끝나는 시간보다 뒤거나 같으면
    # 5. 끝나는 시간을 변경시킨다
    # 6. 근데 인원수가 최대한 많은걸 알아야돼서 전체탐색으로 진행해야 함

def isValid(sTime, eTime):
    if(sTime < eTime):
        return False
    else:
        return True
    
def dfs(depth, curCnt, endTime, time_list):
    global maxPepole
    if(depth == n):
        maxPepole = max(maxPepole, curCnt)
        return
    
    for i in range(depth, n):
        if(isValid(time_list[i][0], endTime)):
            dfs(i, curCnt + time_list[i][2], time_list[i][1], time_list)
    else:
        maxPepole = max(maxPepole, curCnt)
        return


n = int(input())
time_list = []

for _ in range(n):
    time = list(map(int,input().split(' ')))
    time_list.append(time)

time_list.sort(key=lambda x : (x[1],-(x[1]-x[0]),-x[2]))

maxPepole = -1
dfs(0,0,0,time_list)

print(maxPepole)