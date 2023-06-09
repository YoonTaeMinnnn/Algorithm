def solution(s):
    answer = ''
    s = s.split(' ')
    max_s = -247000000
    min_s = 247000000
    for i in s:
        a = int(i)
        if a > max_s:
            max_s = a
        if a < min_s:
            min_s = a
    answer += str(min_s)
    answer += " "
    answer += str(max_s)
    return answer