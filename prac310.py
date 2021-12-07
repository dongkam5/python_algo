#프로그래머스 올바른 괄호
def solution(s):
    answer = True
    lst=[]
    for i in s:
        if i=='(':
            lst.append(1)
        else:
            if lst:
                lst.pop()
            else:
                answer=False
                return answer
    if lst:
        answer=False
    else:
        answer=True
    return answer