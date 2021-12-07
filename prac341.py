#프로그래머스 주식가격
def solution(prices):
    answer = [0]*(len(prices))
    lst=[]
    for i in range (len(prices)):
        lst.append([i,prices[i]])
    stack=[]
    for i in range(len(prices)):
        if stack:
            k=prices[i]
            while stack and stack[-1][1]>k:
                x=stack.pop()
                answer[x[0]]=(i-x[0])
        stack.append(lst[i])
    for ind in range (len(stack)):
        answer[stack[ind][0]]=(i-stack[ind][0])
    return answer