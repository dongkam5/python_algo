# 프로그래머스 level2 연속된 부분 수열의 합
def solution(sequence, k):
    answer = []
    start=0
    end=0
    temp=0
    while end<len(sequence):
        if temp<k: #현재 값이 k보다 작으면
            temp+=sequence[end] #맨 끝 값을 하나 더함
            end+=1
        elif temp==k: # 현재 값이 k와 같으면
            answer.append((start,end-1)) # start부터 end-1 까지 더하였으므로, answer에 (start,end-1) 추가
            temp-=sequence[start] # 맨 앞의 값을 하나 뺌
            start+=1
        elif temp>k: #현재 값이 k보다 크면
            temp-=sequence[start] # 맨 앞의 값을 하나 뺌
            start+=1
    while start<end: # 마지막으로 start가 end보다 작을 때
        if temp>k: # 현재 값이 k보다 크면
            temp-=sequence[start]
            start+=1
        elif temp==k: #현재 값이 k와 같으면
            answer.append((start,end-1))
            break
        else: #현재 값이 k 보다 작으면
            break
    answer.sort(key=lambda x:(x[1]-x[0])) # 길이 짧은 순으로 정렬
    return answer[0]
