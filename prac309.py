#프로그래머스 n진수 게임
def solution(n, t, m, p):
    digit={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    answer = ''
    num='0'
    if t==0:
        return num
    else:
        i=1
        while len(num)<(t-1)*m+p: 
            val=i
            s=''
            while val!=0:
               s+=digit[val%n]
               val=val//n
            s=s[::-1]
            num+=s
            i+=1
        for i in range(t):
            answer+=num[i*m+p-1]
        return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))