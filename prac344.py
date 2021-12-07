#프로그래머스 예상 대진표
def solution(n,a,b):
    answer = 0
    a-=1
    b-=1
    while a!=b:
        a//=2
        b//=2
        answer+=1
    return answer