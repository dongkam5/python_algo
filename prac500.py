#프로그래머스 level2 디펜스 게임
import heapq
def solution(n, k, enemy):
    answer = 0
    i=0
    heap=[]
    len_enemy=len(enemy)
    while True:
        # print(n,enemy[i])
        if i==len_enemy:
            return len_enemy
        if n>=enemy[i]:
            heapq.heappush(heap,-enemy[i])
            n-=enemy[i]
        else:
            if k>0:
                if heap:
                    M=-heapq.heappop(heap)
                    if M<enemy[i]:
                        heapq.heappush(heap,-M)
                        k-=1
                        i+=1
                        continue
                    n+=M
                    k-=1
                    continue
                else:
                    k-=1
                    i+=1
                    continue
            else:
                break
        i+=1
    return i
