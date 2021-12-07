#프로그래머스 시저 암호
def solution(s, n):
    s=list(map(str,s))
    for i in range(len(s)):
        if s[i]!=' ':
            if 'Z'>=s[i]>='A':
                if ord(s[i])+n>ord('Z'):
                    s[i]=chr(ord(s[i])+n-ord('Z')+ord('A')-1)
                else:
                    s[i]=chr(ord(s[i])+n)    
            else:
                if ord(s[i])+n>ord('z'):
                    s[i]=chr(ord(s[i])+n-ord('z')+ord('a')-1)
                else:
                    s[i]=chr(ord(s[i])+n)
    answer =''.join(s)
    return answer