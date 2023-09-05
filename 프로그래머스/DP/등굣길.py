def solution(m, n, puddles):
    answer = 0
    
    v = [[1]*m for _ in range(n)]
    
    check = False
    
    for puddle in puddles:
        y, x = puddle
        v[x-1][y-1] = 0
    
    for i in range(len(v)):
        if v[i][0] == 0:
            check = True
        if check:
            v[i][0] = 0
    
    check = False
    
    for i in range(len(v[0])):
        if v[0][i] == 0:
            check = True
        if check:
            v[0][i] = 0

    for i in range(1,len(v)):
        for j in range(1,len(v[0])):
            if v[i][j] == 0:
                continue
            v[i][j] = (v[i-1][j] + v[i][j-1]) % 1000000007
        
    return v[n-1][m-1] % 1000000007