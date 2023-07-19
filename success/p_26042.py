from collections import deque

n = int(input())

line = deque([])
max_stu = 0 
last_stu = 0

for _ in range(n):
    ty = list(map(int,input().split()))
    
    if ty[0] == 1:
        line.append(ty[1])
        

        if len(line) >= max_stu:
            if len(line) == max_stu:
                if line[-1] < last_stu:
                    last_stu = line[-1]
            elif len(line) > max_stu:
                max_stu = len(line)
                last_stu = line[-1]

                
                
    elif ty[0] == 2:
        line.popleft()
print('{} {}'.format(max_stu, last_stu))