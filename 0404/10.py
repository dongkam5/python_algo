# 프로그래머스 level2 뒤에 있는 큰 수 찾기
def solution(numbers):
    answer = [-1] * (len(numbers)) #전체 -1로 세팅
    stack=[] #값을 임시로 저장할 스택
    for i in range(len(numbers)-1):
        now=numbers[i] #현재 값
        next=numbers[i+1] #다음 값
        if now>=next: #현재 값 >= 다음 값 이면
            stack.append((i,now)) # 스택에 현재 인덱스, 현재 값 저장
        else: #현재 값< 다음 값이면
            answer[i]=next #answer[i]에 다음 값 저장
            while stack: # 스택이 있다면
                idx,val=stack.pop() #스택의 값을 pop 해서
                if val<next: #값이 다음 값(i+1번째 값)보다 작으면
                    answer[idx]=next # answer[idx]값 갱신
                else:
                    stack.append((idx,val)) # 그렇지 않다면, 다시 스택에 삽입
                    break
    return answer

# print(solution([2,3,3,5]))
# print(solution([9, 1, 5, 3, 6, 2]))
