def solution(n, weak, dist):
    dist.sort(reverse=True)
    cnt = 0
    for d in dist:
        if len(weak) == 0:
            break
        
        cnt += 1
        removeIdx = []
        for w in weak:
            for i in [-1, 1]:
                cur = []
                scale = w + d * i
                if 0 <= scale < n:
                    for k in range(len(weak)):
                        if w <= weak[k] <= scale:
                            cur.append(weak[k])
                elif scale < 0:
                    for k in range(len(weak)):
                        if 0 <= weak[k] <= w or n > weak[k] >= n + scale:
                            cur.append(weak[k])
                elif scale > n:
                    for k in range(len(weak)):
                        if w <= weak[k] < n or 0 <= weak[k] <= scale - n:
                            cur.append(weak[k])
                if len(removeIdx) < len(cur):
                    removeIdx = cur
        for rm in removeIdx:
            weak.remove(rm)
        
    return cnt