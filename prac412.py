# 프로그래머스 야근 지수
import heapq


def solution(n, works):
    answer = 0
    q = []
    s = sum(works)
    for work in works:
        heapq.heappush(q, -work)
    if n >= s:
        answer = 0
    else:
        for i in range(n):
            work = heapq.heappop(q)
            work += 1
            heapq.heappush(q, work)
        for work in q:
            answer += (work**2)
    return answer


print(solution(4, [4, 3, 3]))
