#프로그래머스 추석 트래픽
def solution(lines):
    answer = 0
    time=[]
    for line in lines:
        f,s,spend=map(str,line.split())
        hour,min,sec=map(str,s.split(':'))
        sec,msec=sec.split('.')
        spend=float(spend[:-1])
        S=int(hour)*3600+int(min)*60+int(sec)+float(msec)*(0.001)
        if S-spend+0.001<0:
            start=0.0
        else:
            start=S-spend+0.001
        time.append([start,S])
    for i in range(len(time)):
        ans=1
        cri=time[i][1]+1
        j=i+1
        while j<len(time):
            if cri>time[j][0]:
                ans+=1
            j+=1
        answer=max(ans,answer)
    return answer