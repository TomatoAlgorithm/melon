import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    sudoku = []
    zeroPoint = []
    for i in range(9):
        sudoku.append(map(int,input().split(' ')))
        for idx, s in enumerate(sudoku[i], 0):
            if(s == 0):
                zeroPoint.append((i,idx))
    
    while(len(zeroPoint) != 0):
        for zp in zeroPoint:
            rows = sudoku[zp[0]]
            cols = list(zip(*sudoku))[zp[1]]
            if(rows.count(0) == 1):
                for i in range(1,10):
                    if(rows.count(i)==0):
                        sudoku[zp[0]][zp[1]] = i
                        break
                zeroPoint.remove(zp)
            elif(cols.count(0) == 1):
                for i in range(1,10):
                    if(cols.count(i)==0):
                        sudoku[zp[0]][zp[1]] = i
                        break
                zeroPoint.remove(zp)
            else:
                xArea = []
                yArea = []
                area = []
                if zp[0] in (0,1,2):
                    xArea = [0,1,2]
                elif zp[0] in (3,4,5):
                    xArea = [3,4,5]
                else:
                    xArea = [6,7,8]
                if zp[1] in (0,1,2):
                    yArea = [0,1,2]
                elif zp[1] in (3,4,5):
                    yArea = [3,4,5]
                else:
                    yArea = [6,7,8]
                for x in xArea:
                    for y in yArea:
                        area.append(sudoku[x][y])
                if(area.count(0) == 1):
                    for i in range(1,10):
                        if(cols.count(i)==0):
                            sudoku[zp[0]][zp[1]] = i
                            break
                    zeroPoint.remove(zp)
                else:
                    continue
    
    for s in sudoku:
        print(*s,sep=' ')

             
    
