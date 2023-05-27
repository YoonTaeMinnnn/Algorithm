def solution(t, p):
    answer = 0
    s1 = len(t)
    s2 = len(p)
    for i in range(s1-s2+1):
        com = int(t[i:i+s2])
        if com <= int(p):
            answer += 1
    return answer