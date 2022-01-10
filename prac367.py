#프로그래머스 수식 최대화
def solution(expression):
    from itertools import permutations
    answer = 0
    lst=[]
    j=0
    for i in range(len(expression)):
        if not expression[i].isdigit():
            lst.append(expression[j:i])
            lst.append(expression[i])
            j=i+1
    lst.append((expression[j:]))
    permu=permutations([1,2,3],3)
    for a,b,c in permu:
        p={'+':a,'-':b,'*':c}
        number=[]
        symbol=[]
        for val in lst:
            if val.isdigit():
                number.append(int(val))
            else:
                if symbol:
                    if p[symbol[-1]]>=p[val]:
                        while symbol and p[symbol[-1]]>=p[val]:
                            x=symbol.pop()
                            r=number.pop()
                            l=number.pop()
                            if p[x]==a:
                                number.append(l+r)
                            elif p[x]==b:
                                number.append(l-r)
                            elif p[x]==c:
                                number.append(l*r)
                symbol.append(val)
        while symbol:
            x=symbol.pop()
            r=number.pop()
            l=number.pop()
            if p[x]==a:
                number.append(l+r)
            elif p[x]==b:
                number.append(l-r)
            elif p[x]==c:
                number.append(l*r)
        answer=max(answer,abs(number[0]))

    return answer
print(solution("100-200*300-500+20"))
#print(solution("200-300-500-600*40+500+500"))