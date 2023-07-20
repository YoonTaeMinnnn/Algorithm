from itertools import combinations
def solution(orders, course):
    answer = []
   
    
    s = set()
    for i in course:
        cnt = 0
        d = dict()
        for order in orders:
            l = list(combinations(order, i))
            for case in l:
                case = list(case)
                case.sort()
                case = ''.join(case)
                d[case] = d.get(case, 0) + 1
        m = max(list(d.values()), default = -1)
        if m >= 2:
            for key, value in d.items():
                if value == m:
                    answer.append(key)
          
    answer.sort()     
    return answer