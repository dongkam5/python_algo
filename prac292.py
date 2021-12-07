#프로그래머스 조이스틱
def solution(name):
    answer = 0
    lst=list(map(str,name))
    idx=[]
    for i in range(len(lst)):
        if lst[i]!='A':
            idx.append(i)
    ind=0
    while len(idx)!=0:
        if ind>idx[0]:
            if abs(idx[0]-ind)<=abs(idx[-1]-ind):
                answer+=abs(idx[0]-ind)
                ind=idx[0]
                idx.pop(0)
                answer=answer+min(ord(lst[ind])-ord('A'),ord('Z')-ord(lst[ind])+1)
            else:
                answer+=abs(idx[-1]-ind)
                ind=idx[-1]
                idx.pop(-1)
                answer=answer+min(ord(lst[ind])-ord('A'),ord('Z')-ord(lst[ind])+1)
        elif ind<idx[0]:
            if abs(idx[0]-ind)<=abs(ind+len(lst)-idx[-1]):
                answer+=abs(idx[0]-ind)
                ind=idx[0]
                idx.pop(0)
                answer=answer+min(ord(lst[ind])-ord('A'),ord('Z')-ord(lst[ind])+1)
            else:
                answer+=abs(ind+len(lst)-idx[-1])
                ind=idx[-1]
                idx.pop(-1)
                answer=answer+min(ord(lst[ind])-ord('A'),ord('Z')-ord(lst[ind])+1)
        else:
            ind=idx[0]
            idx.pop(0)
            answer=answer+min(ord(lst[ind])-ord('A'),ord('Z')-ord(lst[ind])+1)
    return answer
