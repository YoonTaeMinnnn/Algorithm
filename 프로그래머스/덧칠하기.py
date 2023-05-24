def solution(n, m, section):
    answer = 0
    cnt = 0
    a = 0
    for i in section:
        if i > a:
            cnt += 1
            a = i + (m-1)

    return cnt