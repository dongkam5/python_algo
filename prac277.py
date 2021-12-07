#프로그래머스 이상한 문자 만들기
def solution(s):
    ind=0
    s=list(map(str,s))
    for i in range(len(s)):
        if s[i]==' ':
            ind=0
            continue
        else:
            if ind%2==0:
                ind+=1
                s[i]=s[i].upper()
            else:
                s[i]=s[i].lower()
                ind+=1
    answer = ''.join(s)
    return answer

print(solution("try hello world"))