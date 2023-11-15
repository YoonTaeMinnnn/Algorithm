from itertools import product
def solution(word):
    answer = 0
    l = []
    for i in range(1,6):
        for j in product(['A','E','I','O','U'], repeat = i):
            l.append(''.join(list(j)))
    l.sort()

    return l.index(word) + 1