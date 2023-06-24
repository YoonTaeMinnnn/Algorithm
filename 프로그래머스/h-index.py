def solution(citations):
    answer = 0
    
    def test(m):
        cnt = 0
        for i in citations:
            if i >= m:
                cnt += 1
        if cnt >= m:
            return True
        return False
    
    lt = 0
    rt = max(citations)
    res = 0
    
    while lt <= rt:
        mid = (lt+rt) // 2
        if test(mid):
            lt = mid + 1
            res = mid
        else:
            rt = mid - 1
    
    return res