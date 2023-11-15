# 문자열 정렬 : 앞자리의 크기로 비교 (자릿수x)

def solution(phone_book):
    answer = True
    phone_book.sort()
    s = len(phone_book)
    for i in range(s-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer