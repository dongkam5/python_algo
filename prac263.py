#프로그래머스 갑부어피치

def solution(gems):
    d=len(set(gems))
    bosuk={}
    ans=100000
    for i in range(len(gems)):
        bosuk[gems[i]]=i
        if len(bosuk)==d:
            m=min(bosuk.values())
            M=i
            ans=M-m
            s=m+1
            a=M+1
            break
    i+=1
    while (i<len(gems)):
        if bosuk[gems[i]]==m:
            bosuk[gems[i]]=i
            m=min(bosuk.values())
            M=i
            if M-m<ans:
                ans=M-m
                s=m+1
                a=M+1
        else:
            bosuk[gems[i]]=i
            M=i
        i+=1
    answer = [s,a]
    return answer