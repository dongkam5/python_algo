# 백준 7662 이중 우선순위 큐
import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    heap = []
    for _ in range(int(input())):
        operation, num = input().split()
        num = int(num)
        if operation == 'I':
            heapq.heappush(heap, num)
        elif operation == 'D' and heap:
            if num == -1:
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if heap:
        m = heap[0]
        M = heapq.nlargest(1, heap)[0]
        print(M, m)
    else:
        print('EMPTY')
