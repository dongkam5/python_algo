#프로그래머스 영어 끝말잇기

def solution(n, words):
    lst=[]
    cnt=-1
    previous=words[0][0]
    for i in range(len(words)):
        if previous==words[i][0]:
            if words[i] not in lst:
                lst.append(words[i])
                previous=words[i][-1]
            else:
                cnt=(i)
                break
        else:
            cnt=(i)
            break
    if cnt==-1:
        answer=[0,0]
    else:
        answer=[(cnt%n)+1,(cnt//n)+1]
    return answer
