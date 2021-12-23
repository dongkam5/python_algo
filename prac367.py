
def solution(orders, course):
    from itertools import combinations
    from collections import Counter
    answer = []
    for c in course:
        temp=[]
        for order in orders:
            combi=combinations(sorted(order),c)
            temp+=combi
        counter=Counter(temp)
        if len(counter) !=0 and max(counter.values())>1:
            answer+=[''.join(f) for f in counter if max(counter.values())==counter[f]]
    return answer
