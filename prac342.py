#프로그래머스 모음사전

def solution(word):
    import sys
    sys.setrecursionlimit(10**6)
    vowels=['A','E','I','O','U']
    global cnt
    global answer
    answer = 0
    cnt=0
    string=''
    def dfs(w):
        global cnt
        global answer
        cnt+=1
        if w==word:
            answer=cnt
        if len(w)==5:
            return
        else:
            for i in range(5):
                dfs(w+vowels[i])
    for i in range(5):
        dfs(vowels[i])
    return answer
