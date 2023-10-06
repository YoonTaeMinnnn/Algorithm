def solution(s):
    answer = 0
    s = list(s)
    l = len(s)
    
    stack = []
    
    for i in range(l):
        if i > 0:
            s.append(s.pop(0))
        for j in s:
            if j == '{' or j =='(' or j =='[':
                stack.append(j)
            else:
                if j =='}':
                    if stack:
                        if stack.pop() != '{':
                            break
                    else:
                        break
                elif j == ']':
                    if stack:
                        if stack.pop() != '[':
                            break
                    else:
                        break
                elif j == ')':
                    if stack:
                        if stack.pop() != '(':
                            break
                    else:
                        break
        else:
            answer += 1
    if stack:
        return 0
    return answer