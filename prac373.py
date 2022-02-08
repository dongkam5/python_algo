#프로그래머스 섬 연결하기
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:(x[2]))
    island={}
    link=0
    for cost in costs:
        a,b,c=cost[0],cost[1],cost[2]
        if a not in island or b not in island:
            island[a]=b
            island[b]=a
            link+=1
            answer+=c
        else:
            if link<n-1:
                link+=1
                answer+=c
            else:
                break
    return answer