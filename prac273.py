#프로그래머스 문자열을 정수로 바꾸기
import sys
def solution(s):
    answer = 0
    if s[0].isdigit():
        answer=int(''.join(s))
    else:
        if s[0]=='+':
            answer=int(''.join(s))
        elif s[0]=='-':
            answer=int(''.join(s))
    return answer