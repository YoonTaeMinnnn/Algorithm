# 딕셔너리 => key값으로 삭제 가능 pop(key)
def solution(topping):
    answer = 0
    l = []
    s = set()
    d = dict()
    for i in topping:
        d[i] = d.get(i, 0) + 1
    left = dict()
    for i in range(len(topping)-1):
        left[topping[i]] = left.get(topping[i], 0) + 1
        d[topping[i]] -= 1
        if d[topping[i]] == 0:
            d.pop(topping[i])
        if len(d.keys()) == len(left.keys()):
            answer += 1
            
    return answer