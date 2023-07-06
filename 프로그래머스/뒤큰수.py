def solution(numbers):
    s = len(numbers)
    answer = [-1] * s
    stack = []
    
    for i in range(s):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    
    return answer