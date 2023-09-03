def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    a = s // n 
    b = s % n
    answer = [a] * n
    if b > 0:
        for i in range(b):
            answer[i] += 1
        answer.sort()
        return answer
    return answer