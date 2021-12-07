#프로그래머스 문자열 다루기 기본
def solution(s):
    answer = True
    if len(s)==4 or len(s)==6:
        a=0
        d=0
        for i in range(len(s)):
            if s[i].isdigit():
                print('dongkam')
                d+=1
            else:
                a+=1
        if (d!=len(s) and a!=len(s)):
            answer=False
    else:
        answer=False
    return answer