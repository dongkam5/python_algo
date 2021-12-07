#프로그래머스 괄호 회전하기
def solution(s):
    answer = 0
    s=list(map(str,s))
    if len(s)%2==1:
        return 0
    else:
        for _ in range(len(s)):
            lst=[]
            for i in range(len(s)):
                lst.append(s[i])
                if len(lst)>1:
                    if lst[-2]=='(' and lst[-1]==')':
                        lst.pop()
                        lst.pop()
                    elif lst[-2]=='{' and lst[-1]=='}':
                        lst.pop()
                        lst.pop()
                    elif lst[-2]=='[' and lst[-1]==']':
                        lst.pop()
                        lst.pop()
            if not lst:
                answer+=1
            s.append(s.pop(0))
        return answer