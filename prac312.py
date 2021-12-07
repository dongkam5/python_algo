#프로그래머스 피로도 완전탐색
import itertools
def solution(k, dungeons):
    answer = 0
    lst=[i for i in range(len(dungeons))]
    permu=itertools.permutations(lst,len(dungeons))
    for l in permu:
        l=list(map(int,l))
        cnt=0
        val=k
        for i in range(len(l)):
            if val>=dungeons[l[i]][0]:
                val-=dungeons[l[i]][1]
                cnt+=1
            else:
                break
        answer=max(answer,cnt)
    return answer
print(solution(80,[[80,50],[31,1],[31,1]]))