#백준 15903 다른풀이
import sys
import heapq

n,m=map(int,sys.stdin.readline().split())
cards=list(map(int,sys.stdin.readline().split()))
heapq.heapify(cards)
for _ in range(m):
    card1=heapq.heappop(cards)
    card2=heapq.heappop(cards)
    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

print(sum(cards))
