def solution(nums):
    n = len(nums)//2
    d = dict()
    for i in nums:
        d[i] = d.get(i, 0) + 1
    if len(d) > n:
        return n
    else:
        return len(d)
    