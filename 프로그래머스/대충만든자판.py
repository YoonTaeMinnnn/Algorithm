import sys
def solution(keymap, targets):
    answer = []
    res = 0
    
    for i in range(len(targets)):
        sum = 0
        for j in range(len(targets[i])):
            word = targets[i][j]
            res = 247000000
            for z in range(len(keymap)):
                for w in range(len(keymap[z])):
                    if word == keymap[z][w]:
                        if w+1 < res:
                            res = w+1
            if res == 247000000:
                answer.append(-1)
                break
            sum += res
        else:
            answer.append(sum)
    
    return answer