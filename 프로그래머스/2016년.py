def solution(a, b):
    answer = ''
    months = [31,29] + [31,30]*2 + [31]*2 + [30,31]*2
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    total = 0
    for i in range(a-1):
        total += months[i]
    total += b
    
    return days[total%7-1]