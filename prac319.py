#프로그래머스 기능개발
def solution(progresses, speeds):
    answer = []
    lst=[0]*(len(progresses))
    for i in range(len(progresses)):
        rest=100-progresses[i]
        if rest%speeds[i]==0:
            lst[i]=((rest//speeds[i]))
        else:
            lst[i]=(rest//speeds[i])+1
    i=0
    while i<(len(lst)-1):
        if lst[i]>=lst[i+1]:
            j=2
            while (i+j)<len(lst) and lst[i]>=lst[i+j]:
                j+=1
            answer.append(j)
            i+=(j-1)
        else:
            answer.append(1)
        i+=1
    if i!=len(lst):
        answer.append(1)
    return answer
