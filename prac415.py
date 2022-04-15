# 프로그래머스 줄 서는 방법
import math


def solution(n, k):
    answer = []
    k -= 1
    lst = [i for i in range(1, n+1)]
    while n > 1:
        p = math.perm(n-1)
        answer.append(lst.pop(int(k//p)))
        k = k % p
        n -= 1
    for val in lst:
        answer.append(val)
    return answer


print(solution(3, 5))
