#프로그래머스 level2 귤 고르기
from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    cnt=[]
    dic=defaultdict(int)
    for t in tangerine:
        dic[t]+=1
    for key in dic:
        cnt.append(dic[key])
    cnt.sort(reverse=True)
    i=0
    while k>0:
        answer+=1
        k-=cnt[i]
        i+=1
    return answer
