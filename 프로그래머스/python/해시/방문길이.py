def solution(dirs):
    answer = 0
    s = set()
    x,y = 0,0
    d = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
    for i in dirs:
        dx, dy = d[i]
        nx = x + dx
        ny = y + dy
        if -5<=nx<=5 and -5<=ny<=5:
            s.add(((x,y),(nx,ny)))
            s.add(((nx,ny),(x,y)))
            x = nx
            y = ny
    return len(s) // 2
            
 