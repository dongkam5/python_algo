#프로그래머스 단어변환
def solution(begin, target, words):
    visited=[]
    global answer
    answer=10000
    def dfs(begin):
        global answer
        if begin==target:
            answer=min(answer,len(visited))
            return
        for i in words:
            cnt=0
            for j in range(len(i)):
                if begin[j]==i[j]:
                    cnt+=1
            if cnt==(len(i)-1) and i not in visited:
                visited.append(i)
                dfs(i)
                visited.pop(visited.index(i))
    dfs(begin)
    if answer==10000:
        answer=0
        return answer
    else:
        return answer