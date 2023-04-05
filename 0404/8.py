# 프로그래머스 level2 할인 행사
def solution(want, number, discount):
    answer = 0
    dic=dict()
    l=[]
    
    
    for i in range(len(want)): #초기 값 세팅
        dic[want[i]]=number[i]
    
    
    for i in range(10): # 첫날~10일차까지 할인품목 체크 
        inStuff=discount[i]
        if inStuff in want:
            dic[inStuff]-=1
        l.append(inStuff)
    
    for wantStuff in want: #모두 할인 받는지 체크
        if dic[wantStuff]>0:
            break
    else:
        answer+=1
    
    for i in range(10,len(discount)): # N일차~N+10일차까지 할인품목 체크
        outStuff=l.pop(0)
        if outStuff in want:
            dic[outStuff]+=1
        inStuff=discount[i]
        l.append(inStuff)
        if inStuff in want:
            dic[inStuff]-=1
        for wantStuff in want: #모두 할인 받는지 체크
            if dic[wantStuff]>0:
                break
        else:
            answer+=1
    return answer
