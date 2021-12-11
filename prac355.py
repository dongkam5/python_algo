#프로그래머스 더 맵게
def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    leng=len(scoville)
    while scoville[0]<K and leng>1:
        x1=heapq.heappop(scoville)
        x2=heapq.heappop(scoville)
        new= x1+x2*2
        heapq.heappush(scoville,new)
        leng-=1
        answer+=1
    if scoville[0]>=K:
        return answer
    else:
        return -1