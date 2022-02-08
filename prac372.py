#프로그래머스 단속카메라
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:(x[0],x[1]))
    cre=routes[0][1]
    for route in routes:
        if route[0]<=cre:
            if route[1]<=cre:
                cre=route[1]
            else:
                continue
        else:
            answer+=1
            cre=route[1]
    return answer+1
