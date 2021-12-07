#프로그래머스 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks=[0]*(bridge_length)
    s=0
    while truck_weights:
        answer+=1
        s-=trucks.pop(0)
        check=0
        if s+truck_weights[0]<=weight:
            check=1
            start=truck_weights.pop(0)
            s+=start
            trucks.append(start)
        if check==0:
            trucks.append(0)
    answer+=bridge_length
    return answer
