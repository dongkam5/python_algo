def solution(book_time):
    answer = 0
    bts=[] # 분으로 변환한 시간들을 저장할 list
    for bt in book_time: # 각시간에 대해
        start,end=bt # 시작 시간, 끝 시간을 받음
        start_h,start_min=map(int,start.split(':'))
        start_t=start_h*60+start_min #시작 시간을 분 단위로 표현
        end_h,end_min=map(int,end.split(':'))
        end_t=end_h*60+end_min # 끝 시간을 분 단위로 표현
        bts.append([start_t,end_t]) # 리스트에 추가
    bts.sort() #정렬
    outs=[] # 아직 퇴실하지 않은 방들
    for bt in bts:
        start_t,end_t=bt 
        for i in range(len(outs)):
            if outs[i]+10>start_t: # 만약, 퇴실시간 + 10분 > 새로이 입실하는 고객의 시간
                outs=outs[i:] # 퇴실처리
                break
        else:
            outs.clear() # 반복문이 break 되지 않았으면, (모든 퇴실시간+10분 < 시작시간이므로) 모두 퇴실처리
        if len(outs)>=answer:
            answer+=1
        outs.append(end_t)
        outs.sort() # 퇴실 시간이 빠른 순으로 정렬
    
    return answer
