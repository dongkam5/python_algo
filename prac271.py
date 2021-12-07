#프로그래머스 2016년

def solution(a, b):
    answer = ''
    month=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,12):
        month[i]+=month[i-1]
    days=month[a-1]+b
    day={0:'FRI',1:'SAT',2:'SUN',3:'MON',4:'TUE',5:'WED',6:'THU'}
    answer=day[(days-1)%7-1]
    return answer

a,b=map(int,input().split())
print(solution(a,b))