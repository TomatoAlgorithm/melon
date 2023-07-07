import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    # 회의실 배정 풀이법
    # 1. 강의가 끝나는 시간을 기준으로 오름차순 정렬을 한다
    # 2. 끝나는 시간이 같다면 강의시간이 더 짧은 순서로 정렬을 한다(시작과 동시에 끝나는 수업이 있기 때문에)
    # 3. 이렇게 정렬이 되면 강의가 끝나는 시간을 변수에 저장한다
    # 4. 그 다음 리스트를 순회하며 정렬된 강의들의 시작시간을 비교해서 끝나는 시간보다 뒤거나 같으면
    # 5. 끝나는 시간을 변경시킨다
    n = int(input())
    time_list = []
    
    for _ in range(n):
        time = list(map(int,input().split(' ')))
        time_list.append(time)

    time_list.sort(key=lambda x : (x[1],-(x[1]-x[0])))

    # print(time_list)

    endTime = time_list[0][1]
    cnt = 1
    for i in range(1,n):
        if(time_list[i][0] >= endTime):
            cnt+=1
            endTime = time_list[i][1]
                           
    print(cnt)

    


solution()