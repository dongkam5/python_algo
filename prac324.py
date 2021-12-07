#프로그래머스 프린터
def solution(priorities, location):
    m=max(priorities)
    leng=len(priorities)
    answer = 0
    while priorities:
        val=priorities.pop(0)
        if m>val:
            priorities.append(val)
            if location==0:
                location=(leng-1)
            else:
                location-=1
        else:
            if location==0:
                answer+=1
                break
            else:
                m=max(priorities)
                leng-=1
                location-=1
                answer+=1
    return answer

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))