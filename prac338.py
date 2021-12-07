#프로그래머스 이진 변환 반복하기
def solution(s):
    s=list(map(str,s))
    leng=len(s)
    i=0
    zero_cnt=0
    cnt=0
    while True:
        while i<leng:
            if s[i]=='0':
                s.pop(i)
                leng-=1
                zero_cnt+=1
            else:
                i+=1
        cnt+=1
        if len(s)==1 and s[0]=='1':
            break
        else:
            a=bin(len(s))[2:]
            s=list(map(str,str(a)))
            leng=len(s)
            i=0
    answer=[cnt,zero_cnt]
    return answer

print(solution("110010101001"))