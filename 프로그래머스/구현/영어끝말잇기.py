def solution(n, words):
    answer = []

    com = words[0][-1]
    for i in range(1, len(words)):
        if com != words[i][0] or words[i] in words[:i]:
            if (i+1)%n == 0:
                answer.append([n, (i+1)//n])
            else:
                answer.append([(i+1)%n, (i+1)//n + 1])
            break
        com = words[i][-1]
    else:
        answer.append([0,0])
        

    return answer[0]