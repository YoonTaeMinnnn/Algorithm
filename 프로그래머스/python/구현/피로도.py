from itertools import permutations
def solution(k, dungeons):
    answer = -1
    m = -247000000
    l = list(permutations(dungeons,len(dungeons)))
    for i in l:
        com = k
        cnt = 0
        for j in i:
            if j[0] > com:
                break
            else:
                cnt += 1
                com -= j[1]
        if cnt > m:
            m = cnt

    return m
