#프로그래머스 [1차] 캐시

def solution(cacheSize, cities):
    answer = 0
    for i in range(len(cities)):
        cities[i]=cities[i].upper()
    lst=[]
    for i in range(len(cities)):
        if cities[i] in lst:
            ind=lst.index(cities[i])
            lst.append(lst.pop(ind))
            answer+=1
        else:
            lst.append(cities[i])
            if len(lst)>cacheSize:
                lst.pop(0)
            answer+=5
    return answer