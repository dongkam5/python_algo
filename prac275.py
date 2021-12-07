#프로그래머스 하샤드 수
def solution(x):
    lst=list(map(int,str(x)))
    s=0
    for i in range(len(lst)):
        s+=lst[i]
    if (x%s)==0:
        answer = True
    else:
        answer=False
    return answer
print(solution(10))