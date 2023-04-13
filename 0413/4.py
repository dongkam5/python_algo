#프로그래머스 level2 마법의 엘리베이터
def solution(storey):
    answer = 0
    storey=str(storey)
    list_=list(map(int,storey))
    for i in range(len(list_)-1,0,-1):
        if list_[i]>5: # 현재 숫자가 5보다 크면 올림
            answer+=10-list_[i]
            list_[i-1]+=1
        elif list_[i]==5 and list_[i-1]>=5: # 현재 숫자가 5이고, 바로 앞자리의 숫자가 5 이상이면 올림
            answer+=10-list_[i]
            list_[i-1]+=1
        else: # 현재 숫자가 5보다 작거나, 현재 숫자가 5이고, 바로 앞자리의 숫자가 5 미만이면 내림
            answer+=list_[i]
    if list_[0]>5: # 맨 앞자리 숫자가 5보다 크면
        answer+=10-list_[0]
        answer+=1
    else:
        answer+=list_[0] # 맨 앞자리 숫자가 5보다 작거나 같으면
    return answer
