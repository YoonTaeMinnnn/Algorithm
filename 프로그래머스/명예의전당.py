def solution(k, score):
    answer = []
    best = []
    for i in range(len(score)):
        if i < k:
            best.append(score[i])
            answer.append(min(best))
            print(answer)
        else:
            best.sort(reverse= True)
            if best[-1] < score[i]:
                best.pop()
                best.append(score[i])
            answer.append(min(best))
            
    return answer