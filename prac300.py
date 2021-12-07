#프로그래머스 N개의 최소공배수

def solution(arr):
    import math
    answer = 1
    for i in range(len(arr)):
        answer=answer*arr[i]//math.gcd(answer,arr[i])
    return answer