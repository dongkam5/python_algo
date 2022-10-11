# 프로그래머스 level2 두 큐 합 같게 만들기
from collections import deque
import sys
input = sys.stdin.readline


def solution(queue1, queue2):
    answer = 0
    size = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    while s1 != s2:
        if answer > size*3:
            return -1
        if s1 > s2:
            val = queue1.popleft()
            s1 -= val
            s2 += val
            queue2.append(val)
            answer += 1
        else:
            val = queue2.popleft()
            s1 += val
            s2 -= val
            queue1.append(val)
            answer += 1
    return answer


# print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
