def solution(arr):
    answer = 0
    com = 1
    arr.sort(reverse = True)
    while True:
        a = arr[0] * com
        cnt = 0
        for i in range(1, len(arr)):
            if a % arr[i] == 0:
                cnt += 1
            else:
                break
        if cnt == len(arr) - 1:
            return a
        else:
            com += 1
        
                
    return answer