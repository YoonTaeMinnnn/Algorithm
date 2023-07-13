from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    today_year = int(today.split('.')[0])
    today_month = int(today.split('.')[1])
    today_day = int(today.split('.')[2])
    
    d = dict()
    for t in terms:
        term = t.split()[0]
        ex = t.split()[1]
        d[term] = int(ex)
    
    for i in range(len(privacies)):
        year = int(privacies[i].split('.')[0])
        month = int(privacies[i].split('.')[1])
        day = int(privacies[i].split('.')[2].split()[0])
        term = privacies[i].split('.')[2].split()[1]
        ex = d[term]
        if ex+month > 12:
            year = year + (ex+month) // 12
            month = (ex+month) % 12 
            if month == 0:
                year -= 1
                month = 12
            if day == 1:
                month -= 1
                day = 28
            else:
                day = day - 1
        else:
            month = month + ex
            if day == 1:
                month -= 1
                day = 28
            else:
                day = day - 1
        print(year, month, day)     
        if today_year > year:
            answer.append(i+1)
        elif today_year == year:
            if today_month > month:
                answer.append(i+1)
            elif today_month == month:
                if today_day > day:
                    answer.append(i+1)
        
    return answer