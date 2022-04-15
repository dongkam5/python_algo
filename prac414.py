# 프로그래머스 최고의 집합

def solution(n, s):
    answer = []
    if n > s:
        answer.append(-1)
    else:
        stan = s//n
        left = s % n
        for i in range(n-left):
            answer.append(stan)
        for i in range(left):
            answer.append(1+stan)
    return answer


print(solution(3, 11))
