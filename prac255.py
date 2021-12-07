#프로그래머스 타겟 넘버
def solution(numbers, target):
    global answer
    answer=0
    def dfs(number,i):
        global answer
        if i==len(numbers):
            if number==target:
                answer+=1
            return
       
        dfs(number+numbers[i],i+1)
        dfs(number-numbers[i],i+1)
        
    dfs(numbers[0],1)
    dfs(-numbers[0],1)
    return answer