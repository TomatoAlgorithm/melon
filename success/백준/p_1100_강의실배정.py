import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

def solution():
    # 강의실 배정 풀이법
    # 1. 회의실 배정이랑 결이 같지만 풀이법이 더 복잡하다(시간이 겹치면 강의실 개수를 늘리는 방법)
    # 2. 강의시간을 입력받아 강의가 끝나는 시간을 기준으로 오름차순 정렬시킨다
    # 3. 첫번째 강의의 끝나는 시간을 heapQ에 push시킨다.
    # 4. 리스트를 순회하며 강의의 시작시간을 heapQ의 첫번째 들어있는 끝나는 시간과 비교한다.
    # 5. 끝나는 시간보다 시작시간이 뒤거나 같으면 첫번째 끝나는 시간을 pop시키고 
    # 6. 해당강의가 끝나는 시간을 heapPush시킨다 -> 이러면 현재 heap에 배정되어있는 강의가 끝나는 순서대로 정렬된다.
    # 어차피 강의는 끝나는 시간을 기준으로 오름차순 정렬이 되어 있기 때문에 heap에서 뒤로 밀린 강의보다 앞일 수 없다
    # 7. 위 4~6을 반복하고 난 뒤 heapQ에 저장된 요소의 개수가 강의실 개수가 된다.
    time_list = []

    for _ in range(n):
        time = list(map(int,input().split(' ')))
        time_list.append(time)

    time_list.sort()

    pQ = list()
    heapq.heappush(pQ, time_list[0][1])

    for i in range(1,n):
        if time_list[i][0] >= pQ[0]:
            heapq.heappop(pQ)
        heapq.heappush(pQ, time_list[i][1])
    
            
    print(len(pQ))


solution()