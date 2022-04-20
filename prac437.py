# 프로그래머스 징검다리 건너기
from collections import deque


def solution(stones, k):
    answer = (1e9)
    if k == 1:
        return min(stones)
    else:
        q = deque(stones[0:k])
        M = max(q)
        answer = min(answer, M)
        for i in range(0, len(stones)-k):
            out_ = q.popleft()
            if out_ == M:
                M = max(q)
            in_ = stones[i+k]
            if in_ > M:
                M = in_
            q.append(in_)
            answer = min(M, answer)
        return answer


print(solution([2, 3],	1))
