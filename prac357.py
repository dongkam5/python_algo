#프로그래머스 튜플

def solution(s):
    answer = []
    i=1
    lst=[]
    while i<(len(s)-1):
        if s[i]=='{':
            arr=[]
            j=1
            while s[i+j]!='}':
                j+=1
            arr=list(map(int,s[i+1:i+j].split(',')))
            i+=j
            lst.append(arr)
        i+=1
    lst.sort(key=lambda x:(len(x)))
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] not in answer:
                answer.append(lst[i][j])
    return answer

#print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
print(solution("{{123}}"))