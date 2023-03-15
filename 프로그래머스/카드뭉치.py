def solution(cards1, cards2, goal):
    answer = ''
    answerr = ''
    for i in goal:
        if i in cards1:
            if cards1.pop(0) != i:
                answerr += "No"
                return answerr
        if i in cards2:
            if cards2.pop(0) != i:
                answerr += "No"
                return answerr
    answer += "Yes"     
    return answer