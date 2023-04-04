# 프로그래머스 level1 삼총사
from itertools import combinations
def solution(number):
    answer = 0
    combi=combinations(number,3)
    for c in combi:
        if sum(c)==0:
            answer+=1
    return answer
