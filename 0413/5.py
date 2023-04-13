#프로그래머스 level2 요격 시스템
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[0],x[0]-x[1]))
    i=0
    while i<len(targets):
        t_start,t_end=targets[i] # 첫 미사일의 시작점, 끝점 파악
        j=1
        while i+j<len(targets): 
            if t_end>targets[i+j][0]: # 현재 끝점 > 나중 미사일의 시작점
                if t_end>targets[i+j][1]: # 현재 끝점 > 나중 미사일의 끝점
                    t_end=targets[i+j][1] # 현재 끝점을 나중 미사일의 끝점으로 갱신
                j+=1
            else:
                break
        i=i+j
        answer+=1
    return answer
