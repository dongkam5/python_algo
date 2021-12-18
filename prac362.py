#프로그래머스 [1차] 뉴스 클러스터링

def makepair(s):
    lst=[]
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            lst.append(s[i]+s[i+1])
    return lst
def solution(str1, str2):
    answer = 0
    str1=makepair(str1.upper())
    str2=makepair(str2.upper())
    str1.sort()
    str2.sort()
    intersect=[]
    i=0
    j=0
    while str1 and str2 and i<len(str1) and j<len(str2):
        if str1[i]==str2[j]:
            intersect.append(str1[i])
            i+=1
            j+=1
        elif str1[i]>str2[j]:
            j+=1
        else:
            i+=1
    Union=str1+str2
    for i in range(len(intersect)):
        Union.pop(Union.index(intersect[i]))
    if len(Union)!=0:
        jac=len(intersect)/len(Union)
        answer=int(jac*65536)
        return answer    
    else:
        if str1==str2:
            return 65536

print(solution("french","FRENCH"))