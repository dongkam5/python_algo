#프로그래머스 2개 이하로 다른 비트
def solution(numbers):
    from collections import deque
    answer = []
    for number in numbers:
        bit=bin(number)[2:]
        bit=deque(list(map(str,bit)))
        zero_cnt=bit.count('0')
        leng=len(bit)
        if zero_cnt==0:
            bit.appendleft('1')
            bit[1]='0'
        elif zero_cnt==1:
            ind=bit.index('0')
            if ind==(len(bit)-1):
                bit[ind]='1'
            else:
                bit[ind]='1'
                bit[ind+1]='0'
        else:
            for i in range(len(bit)-1,0,-1):
                if bit[i]=='0':
                    break
            if i==(len(bit)-1):
                bit[i]='1'
            else:
                bit[i]='1'
                bit[i+1]='0'
        answer.append(int(''.join(bit),2))
    return answer