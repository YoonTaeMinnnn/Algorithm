def solution(s):
    answer = ''
    s = s.split(' ')
    print(s)
    for i in range(len(s)):
        s[i] = s[i].capitalize()
        # capitalize() : 첫글자 대 -> 소, 소 -> 대, 알파벳x->무시, 나머지는 모두 소문자
    answer = ' '.join(s)
    # join : 문자열 or 리스트 사이에 문자 삽입 -> 문자열 리턴
                    

            
    return answer