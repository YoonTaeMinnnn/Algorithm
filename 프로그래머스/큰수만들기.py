def solution(number, k):
    answer = ''
    number = list(number)
    stack = []

    for i in number:
        while stack and i > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
        
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)