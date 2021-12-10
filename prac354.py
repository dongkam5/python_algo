#프로그래머스 오픈채팅방
def solution(record):
    answer = []
    lst={}
    prompt=[]
    for line in record:
        s=list(map(str,line.split()))
        if s[0]!='Leave':
            lst[s[1]]=s[2]
        prompt.append(s)
    for line in prompt:
        if line[0]=='Enter':
            answer.append("{}님이 들어왔습니다.".format(lst[line[1]]))
        elif line[0]=='Leave':
            answer.append("{}님이 나갔습니다.".format(lst[line[1]]))
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))