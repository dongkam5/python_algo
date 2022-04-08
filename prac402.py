# 프로그래머스 이중우선순위큐

import heapq

# 프로그래머스 이중우선순위큐


def solution(operations):
    answer = []
    heap = []
    for operation in operations:
        oper, digit = map(str, operation.split())
        if oper == 'I':
            heapq.heappush(heap, int(digit))
        elif heap and oper == 'D' and digit == '1':
            heap = heapq.nlargest(len(heap), heap)[1:]
            heapq.heapify(heap)
        elif heap and oper == 'D' and digit == '-1':
            heapq.heappop(heap)
    if heap:
        M = heapq.nlargest(len(heap), heap)[0]
        heapq.heapify(heap)
        answer.append(M)
        answer.append(heap[0])
    else:
        answer.append(0)
        answer.append(0)
    return answer


# print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
