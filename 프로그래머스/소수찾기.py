from itertools import permutations
def solution(numbers):
    answer = 0
    
    def count(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True
    numbers = list(numbers)
    
    v = []
    for i in range(1,len(numbers)+1):
        l = list(permutations(numbers, i))
        for j in l:
            s = ''
            for x in j:
                s += str(x)
            if int(s) in v:
                continue
            else:
                v.append(int(s))
            if count(int(s)):
                answer += 1
    
    
    return answer