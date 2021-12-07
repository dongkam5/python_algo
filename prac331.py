#프로그래머스 압축

def solution(msg):
    msg=list(map(str,msg))
    answer = []
    dic={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    i=0
    while i<len(msg):
        s=''
        s+=msg[i]
        while i<(len(msg)-1) and s in dic:
            i+=1
            s+=msg[i]
        if len(s)==1:
            answer.append(dic[s])
            i+=1
        elif s in dic:
            answer.append(dic[s])
            i+=1
        else:
            answer.append(dic[s[:-1]])
            dic[s]=len(dic)+1
    return answer
print(solution('KAKAO'))