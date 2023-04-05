# 프로그래머스 level2 연속 부분 수열 합의 개수
from collections import deque
def solution(elements):
    answer = 0
    sets=set()
    for length in range(1,len(elements)+1):
        l=[]
        s=0
        for i in range(-(length),0):
            s+=elements[i]
            l.append(elements[i])
        sets.add(s)
        for i in range(len(elements)):
            sub_=l.pop(0)
            s-=sub_
            s+=elements[i]
            sets.add(s)
            l.append(elements[i])
    answer=len(sets)
    return answer
