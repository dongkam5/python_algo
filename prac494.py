#백준 11286 절댓값 힙
import sys
import heapq #파이썬 힙 라이브러리 사용
input=sys.stdin.readline
N=int(input())
h=[]
for _ in range(N):
    val=int(input())
    if val==0: # 들어온 값이 0이고
        if not h: # 힙이 비어있다면
            print(0) #0 출력
        else: #비어있지 않다면
            print(heapq.heappop(h)[1]) #힙 abs(min) 값을 가지는 요소 출력
    else:
        heapq.heappush(h,[abs(val),val]) # 힙에 추가
