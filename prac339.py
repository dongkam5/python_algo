#프로그래머스 짝지어 제거하기

def solution(s):
    i=0
    lst=[]
    for i in range(len(s)):
        lst.append(s[i])
        if len(lst)>1:
            if lst[-2]==lst[-1]:
                lst.pop()
                lst.pop()
    if lst:
        return 0
    else:
        return 1