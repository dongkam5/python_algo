# 프로그래머스 level1 크기가 작은 부분 문자열
def solution(t, p):
    answer = 0
    len_p=len(p)
    len_t=len(t)
    p=int(p)
    i=0
    while i<len_t-len_p+1:
        temp=t[i:i+len_p]
        if int(temp)<=p:
            answer+=1
        i+=1
    return answer
