# 백준 1966
import sys
input = sys.stdin.readline


def solution(priorities, location):
    m = max(priorities)
    leng = len(priorities)
    answer = 0
    while priorities:
        val = priorities.pop(0)
        if m > val:
            priorities.append(val)
            if location == 0:
                location = (leng-1)
            else:
                location -= 1
        else:
            if location == 0:
                answer += 1
                break
            else:
                m = max(priorities)
                leng -= 1
                location -= 1
                answer += 1
    return answer


for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(arr, M))
