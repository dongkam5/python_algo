#프로그래머스 체육복

def solution(n, lost, reserve):
    lst=[1]*(n+1)
    for i in lost:
        lst[i]-=1
    for i in reserve:
        lst[i]+=1
    for i in range(1,n+1):
        if lst[i]==0 and i==1: 
            if lst[i+1]==2:
                lst[i]=1
                lst[i+1]-=1
        elif lst[i]==0 and i==n:
            if lst[i-1]==2:
                lst[i]=1
                lst[i-1]-=1
        elif lst[i]==0:
            if lst[i-1]==2:
                lst[i]=1
                lst[i-1]-=1
            elif lst[i+1]==2:
                lst[i]=1
                lst[i+1]-=1
    answer = lst.count(1)+lst.count(2)-1
    return answer

print(solution(3,[3],[1]))