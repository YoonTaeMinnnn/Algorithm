def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s = len(answers)
    com1 = a1*(s//5) + a1[:s%5]
    com2 = a2*(s//8) + a2[:s%8]
    com3 = a3*(s//10) + a3[:s%10]
    
    result = [0] * 3
    for i in range(s):
        if answers[i] == com1[i]:
            result[0] += 1
        if answers[i] == com2[i]:
            result[1] += 1
        if answers[i] == com3[i]:
            result[2] += 1
    max_result = max(result)
    if max_result == result[0]:
        answer.append(1)
    if max_result == result[1]:
        answer.append(2)
    if max_result == result[2]:
        answer.append(3)
    return answer