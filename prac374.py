#프로그래머스 섬 연결하기
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:(x[2]))
    link=[]
    for cost in costs:
        a,b,c=cost[0],cost[1],cost[2]
        
    return answer