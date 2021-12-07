#프로그래머스 JadenCase 문자열 만들기

def solution(s):
    answer = ''
    s=s.lower()
    lst=s.split(' ')
    for i in range(len(lst)):
        answer+=(lst[i].capitalize()+' ')
    answer=answer[:-1]
    return answer