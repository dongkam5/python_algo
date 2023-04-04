# 프로그래머스 level1 콜라 문제
def solution(a, b, n):
    answer = 0
    temp=n
    while True:
        answer+=(temp//a)*b
        temp=(temp//a)*b+temp%a
        if temp < a :
            break
    return answer
