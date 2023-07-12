def solution(numbers):
    answer = ''
    numbers = [str(i) for i in numbers]
    numbers.sort(reverse=True, key = lambda x:x*3)
    for i in numbers:
        answer += i
    
    
    return str(int(answer))
    