def solution(s):
    answer = []

    def DFS(n):
        global ch
        if n == 0:
            return
        else:
            ch += str(n % 2)
            DFS(n//2)
    
    n = 0
    cnt = 0
    while s != '1':
        a = ''
        s = list(s)
        l = len(s)
        for i in s:
            if i == '0':
                cnt += 1
                l -= 1
        global ch
        ch = ''
        DFS(l)
        s = ch[::-1] 
        n += 1
        
    return [n, cnt]
