#프로그래머스 예산

def solution(d, budget):
    d.sort()
    answer = 0
    if sum(d)<=budget:
        answer=len(d)
    else:
        i=0
        while budget>=0:
            budget-=d[i]
            i+=1
        answer=i-1
    return answer

''' 다른사람 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
'''