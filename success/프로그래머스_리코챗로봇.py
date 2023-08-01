from collections import deque

endPoint = []

def arrivePoint(maze, visited, x, y, direction):
    while(True):
        dx = x+direction[0]
        dy = y+direction[1]
        
        if((dx < 0 or dx>len(maze[0])-1) or (dy < 0 or dy>len(maze)-1) or maze[dy][dx] == 1):
            break

        x=dx
        y=dy
    
    return [x,y]

def solution(board):
    global endPoint
    maze = []
    visited = []
    startPoint = []
    count = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    for (yIdx,bb) in enumerate(board, 0):
        oneline = []
        oneVisited=[]
        for (xIdx,b) in enumerate(bb, 0):
            if(b == '.'):
                oneline.append(0)
                oneVisited.append(False)
            elif(b == 'D'):
                oneline.append(1)
                oneVisited.append(True)
            elif(b=='R'):
                startPoint.append(xIdx)
                startPoint.append(yIdx)
                startPoint.append(0)
                oneVisited.append(True)
                oneline.append(3)
            elif(b=='G'):
                oneline.append(2)
                oneVisited.append(False)
                endPoint.append(xIdx)
                endPoint.append(yIdx)
        maze.append(oneline)
        visited.append(oneVisited)
    
    deq = deque()
    
    deq.append(startPoint)
    
    while(len(deq) != 0):
        curPoint = deq.popleft()
        
        if(curPoint[0] == endPoint[0] and curPoint[1] == endPoint[1]):
            print(curPoint[2])
            return curPoint[2]
        
        for i in range(4):
            direction = [dx[i],dy[i]]
            getPoint = arrivePoint(maze,visited,curPoint[0],curPoint[1],direction)
            getPoint.append(curPoint[2])
            if(curPoint != getPoint and visited[getPoint[1]][getPoint[0]] == False):
                getPoint[2] = getPoint[2]+1
                deq.append(getPoint)
                visited[getPoint[1]][getPoint[0]] = True
    
    return -1


    
    
solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])