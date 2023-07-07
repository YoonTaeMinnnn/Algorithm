def solution(n):
    answer = 0
    col = 0 #가로
    row = 0 #세로
    if n == 1:
        return 1
    v = [0] * (n+1)
    v[1] = 1
    v[2] = 2
    for i in range(3, n+1):
        v[i] = (v[i-2] + v[i-1]) % 1000000007
    
    return v[n]