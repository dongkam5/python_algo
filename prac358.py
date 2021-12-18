#프로그래머스 메뉴 리뉴얼

def solution(orders, course):
    import itertools
    answer = []
    s=''
    for order in orders:
        s+=order
    s=set(s)
    for i in range(len(course)):
        combi=itertools.combinations(s,course[i])
        M=2
        m=[]
        for c in combi:
            cnt=0
            for order in orders:
                if len(order)>=course[i]:
                    for menu in c:
                        if menu not in order:
                            break
                    else:
                        cnt+=1
            if cnt>M: 
                m=[]
                c=list(c)
                c.sort()
                m.append(''.join(c))
                M=cnt
            elif cnt==M:
                c=list(c)
                c.sort()
                m.append(''.join(c))
        for men in m:
            answer.append(men) 
    answer.sort()
    return answer
