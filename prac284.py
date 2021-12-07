#프로그래머스 [1차] 다트 게임
def solution(dartResult):
    answer = 0
    lst=[0]
    num=0
    i=0
    dartResult=dartResult.replace('10','k')
    while i <len(dartResult):
        if dartResult[i]=='k':
            num=10
        elif dartResult[i].isdigit():
            num=int(dartResult[i])
        elif dartResult[i].isalpha():
            if dartResult[i]=='S':
                lst.append(num)
            elif dartResult[i]=='D':
                lst.append(num**2)
            else:
                dartResult[i]=='T'
                lst.append(num**3)
        elif dartResult[i]=='*':
            lst[-1]*=2
            lst[-2]*=2
        elif dartResult[i]=='#':
            lst[-1]=-lst[-1]
        i+=1
    answer=sum(lst)
    return answer
