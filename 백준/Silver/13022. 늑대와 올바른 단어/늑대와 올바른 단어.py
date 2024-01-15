"""
1. w 갯수를 센다?
2. w 갯수만큼 반복되지 않으면 False
"""

correct = ['w','o','l','f']

word = input()
answer = 1
idx = 0
cnt = 0

while idx < len(word):
    if word[idx] == correct[0]:
        cnt += 1
        idx += 1
    elif word[idx] == correct[1]:
        if cnt == 0:
            print(0)
            exit(0)
        for i in range(1,4):
            for _ in range(cnt):  
                if idx == len(word) or word[idx] != correct[i]:
                    print(0)
                    exit(0)
                idx+=1
        cnt = 0
    else:
        print(0)
        exit(0)
if cnt != 0:
    print(0)
else:
    print(1)