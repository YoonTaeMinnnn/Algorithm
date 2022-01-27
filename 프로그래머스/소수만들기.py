from itertools import combinations
def compare(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    com_list = list(combinations(nums,3))
    result = []
    for i in com_list:
        result.append(sum(i))
    for i in result:
        if compare(i) == True:
            answer+=1
    return answer