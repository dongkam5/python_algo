# 백준 1074 Z
N,r,c,=map(int,input().split()) 
answer=0
def search(r,c,N,tr,tc): # 왼쪽부터 현재 행, 현재 열, 승수, 목표 행, 목표 열
    global answer
    if r==tr and c==tc: #현재 행,열이 목표 행,열이면 함수종료
        return
    half_distance=2**(N-1) #정사각형의 한 변의 절반 길이
    quarter_area=half_distance*half_distance #정사각형 넓이의 4분의 1
    criteria_r,criteria_c=r+half_distance,c+half_distance #4등분했을 때, 구간을 나누는 기준
    if tr<criteria_r: 
        if tc<criteria_c: #왼쪽 위 구간에 있다면
            search(r,c,N-1,tr,tc)
        else: #오른쪽 위 구간에 있다면
            answer+=quarter_area 
            search(r,c+half_distance,N-1,tr,tc)
    else:
        if tc<criteria_c: #왼쪽 아래 구간에 있다면
            answer+=quarter_area*2
            search(r+half_distance,c,N-1,tr,tc)
        else:
            answer+=quarter_area*3 #오른쪽 아래 구간에 있다면
            search(r+half_distance,c+half_distance,N-1,tr,tc)

search(0,0,N,r,c) #탐색 시작

print(answer)