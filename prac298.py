#프로그래머스 신규 아이디 추천

def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    new_id=list(map(str,new_id))
    i=0
    while i<len(new_id):
        if new_id[i].isalnum():
            i+=1
        elif new_id[i]=='_' or new_id[i]=='.' or new_id[i]=='-':
            i+=1
        else:
            new_id.pop(i)
    i=0
    while new_id and new_id[0]=='.':
        new_id.pop(0)
    while new_id and new_id[-1]=='.':
        new_id.pop()
    while i<len(new_id):
        if new_id[i]=='.':
            j=1
            while new_id[i]==new_id[i+j]:
                    j+=1
            for _ in range(j-1):
                new_id.pop(i)
        i+=1
    if len(new_id)==0:
        new_id.append('a')
    if len(new_id)>15:
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id.pop()
    if len(new_id)==1:
        new_id.append(new_id[0])
        new_id.append(new_id[0])
    elif len(new_id)==2:
        new_id.append(new_id[1])
    answer=''.join(new_id)
    return answer

#print(solution('...!@BaT#*..y.abcdefghijklm'))
#print(solution("z-+.^."))
#print(solution("=.="))
#print(solution("123_.def"))
#print(solution("abcdefghijklmn.p"))