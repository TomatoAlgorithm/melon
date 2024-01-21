N = int(input())

balloons = list(map(int, input().split(' ')))
for i in range(N):
    balloons[i] = (balloons[i], i+1)

idx = 0
while balloons:
    direction, number = balloons[idx]
    print(number)
    del balloons[idx]

    remain_N = len(balloons)
    d=1
    if direction < 0:
        direction *= -1
        d = -1
    else:
        idx -= 1
        if idx == -1:
            idx = remain_N-1

    for _ in range(direction):
        idx += 1*d
        if idx == remain_N:
            idx = 0
        elif idx == -1:
            idx = remain_N-1