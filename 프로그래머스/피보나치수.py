def solution(n):
    answer = 0
    l = [0] * (n+1)
    l[0] = 0
    l[1] = 1
    for i in range(2, n+1):
        l[i] = l[i-2] + l[i-1]
    return l[n] % 1234567
    