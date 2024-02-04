"""
문제 접근 방식
A -> N개의 서로 다른 양의 정수
B -> M개의 서로 다른 양의 정수
C -> N개의 배열

C[i] => B에서 A[i]의 가장 가까운 수

T개의 테케
1 <= N,M <= 10^6

B를 정렬한다음에 이분탐색으로 적절한 값 찾기
"""
import sys

input = sys.stdin.readline

def binary_search(val, arr):
    left = 0
    right = len(arr)-1
    diff = 1e9
    ret = 0
    
    while left <= right:
        mid = (left + right) // 2
        arr_val = arr[mid]
        comp_val = abs(val-arr_val)
        if comp_val == 0:
            return arr_val
        
        if comp_val == diff:
            if arr_val < val:
                ret = arr_val
                left = mid+1
            else:
                right = mid-1
        elif comp_val < diff:
            diff = comp_val
            ret = arr_val
            if val < arr_val:
                right = mid-1
            else:
                left = mid+1       
        else:
            if val > arr_val:
                left = mid+1
            else:
                right = mid-1
                
    return ret
            

T = int(input())

for _ in range(T):
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    B.sort()
    
    ans = 0
    
    for i in range(N):
        ans += binary_search(A[i], B)
        
    print(ans)