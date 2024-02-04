"""
0 권한 X
1 실행 O
2 수정 O
3 실행, 수정 O
4 읽기 O
5 읽기, 실행 O
6 읽기, 수정 O
7 읽기, 실행, 수정 O

000
1. 파일 소유자
2. 그룹 소유자
3. 아무것도 아닌애

유저 정보 개수 U
U줄
유저 정보
name => name group에 속함
name group

파일 정보 개수 F
F줄
파일 정보
file_name file_permisiion owner owned_group

질문 갯수 Q
Q줄
user_name file_name operation
"""

import sys
input = sys.stdin.readline

U, F = map(int, input().split(' '))

user_set = set()
group_dict = {}
files = {}

for _ in range(U):
    user_info = list(map(str, input().strip().split(' ')))
    groups = []
    user = user_info[0]
    if len(user_info) >= 2:
        groups = user_info[1]
    
    if user not in group_dict:
        group_dict[user] = set()
        group_dict[user].add(user)

    if groups:
        for group in groups.split(','):
            if group not in group_dict:
                group_dict[group] = set()
            
            group_dict[group].add(user)

for _ in range(F):
    name, permission, owner, owned_group = map(str, input().strip().split(' '))

    files[name] = (permission, owner, owned_group)

Q = int(input())

def checkPermission(op, num):
    # if up == 1:
    #     cur_set.add('X')
    # elif up == 2:
    #     cur_set.add('W')
    # elif up == 3:
    #     cur_set.add('W')
    #     cur_set.add('X')
    # elif up == 4:
    #     cur_set.add('R')
    # elif up == 5:
    #     cur_set.add('R')
    #     cur_set.add('X')
    # elif up == 6:
    #     cur_set.add('R')
    #     cur_set.add('W')
    # elif up == 7:
    #     cur_set.add('R')
    #     cur_set.add('W')
    #     cur_set.add('X')

    # return cur_set
    if num == 7 : return 1
    elif num == 0 : return 0
    elif op == 'R' and num >= 4 : return 1
    elif op == 'W' and num in [2,3,6] : return 1
    elif op == 'X' and num in [1,3,5] : return 1
    else : return 0

for _ in range(Q):
    user_name, file_name, operation = input().strip().split(' ')
    file_permisiion, owner, owned_group = files[file_name]
    owner_auth,group_auth,other_auth = file_permisiion
    if user_name == owner : print(checkPermission(operation, int(owner_auth)))
    elif user_name in group_dict[owned_group] : print(checkPermission(operation, int(group_auth)))
    else : print(checkPermission(operation, int(other_auth)))

    # answer = -1

    # try:
    #     if files[file_name]['owner'] == user_name:
    #         answer = 0
    #     elif user_name in group_dict[files[file_name]['group']]:
    #         answer = 1
    #     elif answer == -1:
    #         answer = 2
    # except:
    #     answer = 2
    # s_permission = set()
    # s_permission = addPermission(s_permission, int(files[file_name]['permission'][answer]))
    # if operation in s_permission:
    #     print(1)
    # else:
    #     print(0)

