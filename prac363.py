#프로그래머스 괄호 변환
def isright(s):
        lst=[]
        for i in range(len(s)):
            if len(lst)>=1:
                if lst[-1]=='(' and s[i]==')':
                    lst.pop()
                else:
                    lst.append(s[i])
            else:
                lst.append(s[i])
        if lst:
            return False
        else:
            return True
def decision(s):
    ans=''
    if not s:
        return ans
    else:
        if isright(s):
            return s
        else:
            l=0
            r=0
            for i in range(len(s)):
                if s[i]=='(':
                    l+=1
                else:
                    r+=1
                if l==r:
                    break
            u=s[:i+1]
            v=s[i+1:]
            if isright(u):
                return ans+u+decision(v)
            else:
                u_=''
                for i in range(1,len(u)-1):
                    if u[i]=='(':
                        u_+=')'
                    else:
                        u_+='('
                return ans+'('+decision(v)+')'+u_
def solution(p):
    answer = ''
    answer=decision(p)
    return answer