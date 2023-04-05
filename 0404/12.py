from collections import defaultdict
def solution(topping):
    answer = 0
    a=defaultdict(int) # 형 롤케잌
    b=defaultdict(int) # 동생 롤케잌
    for t in topping: # 형이 롤케잌 다 가져감
        a[t]+=1
    for t in topping: #제일 끝부터 하나씩 동생에게 떼어줌
        a[t]-=1
        if a[t]==0:
            a.pop(t)
        b[t]+=1
        if len(a)==len(b): #만약 토핑 개수가 같다면
            answer+=1
    
    return answer
