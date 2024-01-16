import sys

input = sys.stdin.readline

def timeCheck(src, trg):
    # 0 => trg < src
    # 1 => trg == src
    # 2 => trg > src
    sH, sM = map(int, src.split(':'))
    tH, tM = map(int, trg.split(':'))
    
    if sH > tH:
        return 0
    elif sH < tH:
        return 2
    else:
        if sM > tM:
            return 0
        elif sM < tM:
            return 2
        else:
            return 1
    
S, E, Q = map(str, input().split(' '))
entered_members = set()
leaved_members = set()

while True:
    try:
        time, nickname = map(str, input().strip().split(' '))
        
        if timeCheck(S, time) <= 1:
            entered_members.add(nickname)
        if timeCheck(E, time) >= 1 and timeCheck(Q, time) <= 1:
            leaved_members.add(nickname)
        
    except:
        break
answer = 0
for member in entered_members:
    if member in leaved_members:
        answer+=1
        
print(answer)