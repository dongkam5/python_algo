#프로그래머스 level2 시소 짝꿍
from collections import defaultdict
def solution(weights):
    answer = 0
    length=len(weights)
    dic=defaultdict(int)
    for weight in weights:
        dic[weight]+=1
    
    for weight in dic.keys():
        if dic[weight]>1:
            answer+= dic[weight]*(dic[weight]-1)//2
        if weight *2 in dic.keys():
            answer+= dic[weight] *dic[weight*2]
        if weight *3/2 in dic.keys():
            answer += dic[weight] * dic[weight*3/2]
        if weight *4/3 in dic.keys():
            answer+=dic[weight]*dic[weight*4/3]
    return answer

print(solution([100,180,360,100,270]))
