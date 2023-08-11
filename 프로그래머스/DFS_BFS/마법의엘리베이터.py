def solution(storey):
    answer = 0
    
    result = []
    def DFS(st, count):
        if st == 0:
            result.append(count)
            return 
        com = st % 10 
        up, down = 10 - com, com
        
        if up < down:
            DFS(st // 10 + 1, count+up)
        elif down < up:
            DFS(st // 10, count+down)
        else:
            for i in range(2):
                DFS(st // 10 + i, count + up)
        
    DFS(storey, 0)
    return min(result)
        
        