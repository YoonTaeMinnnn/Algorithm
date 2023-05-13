def solution(participant, completion):
    d1 = dict()
    d2 = dict()
    for i in participant:
        d1[i] = d1.get(i,0) + 1
    for i in completion:
        d2[i] = d2.get(i,0) + 1
    for key, value in d1.items():
        if d1[key] != d2.get(key,0):
            return key