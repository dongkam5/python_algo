#프로그래머스 실패율
def solution(N, stages):
    answer = []
    stages.sort()
    result=[[0]*2 for _ in range (N+1)]
    for i in range(1,N+1):
        if i in stages:
            result[i][0]=stages.count(i)/len(stages[stages.index(i):])
        result[i][1]=i
    result.pop(0)
    result.sort(key=lambda x:(-x[0],x[1]))
    print(result)
    for i in range(len(result)):
        answer.append(result[i][1])
    return answer

''' 다른사람 풀이
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
'''