#프로그래머스 문자열 압축
def solution(s):
    answer = 0
    for i in range(1,(len(s)//2)+1):
        cnt=1
        lst=[]
        j=0
        previous=''
        while (j+i)<=len(s):
            if s[j:j+i]==previous:
                cnt+=1
            else:
                if cnt!=1:
                    lst.append(cnt-1)
                cnt=1
                previous=s[j:j+i]
            j+=i
        if cnt>1:
            lst.append(cnt-1)
        gain=0
        for k in range(len(lst)):
            gain+=lst[k]*i-len(str(lst[k]+1))
        answer=max(answer,gain)
    return len(s)-answer

print(solution("aabbaccc"))