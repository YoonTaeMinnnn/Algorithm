def solution(n):
    answer = 0
    com = n + 1
    n_com = list(str(format(n,'b')))
    n_count = n_com.count('1')
    while True:
        a = list(str(format(com,'b')))
        if n_count == a.count('1'):
            return com
            break
        com += 1
    