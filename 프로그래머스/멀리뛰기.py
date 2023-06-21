def solution(n):
    answer = 0
    if n <= 2:
        return n
    l = [0] * (n+1)
    l[1] = 1
    l[2] = 2
    for i in range(3, n+1):
        l[i] = l[i-2] + l[i-1]
        
    return l[n] % 1234567