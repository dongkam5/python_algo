#프로그래머스 level2 구명보트

def solution(people,limit):
    answer=0
    people.sort()
    i=0
    j =len(people)-1
    while i<=j:
        answer+=1
        if people[j]+people[i]<=limit:
            i+=1
        j-=1
    return answer
''' 내 코드
def solution(people, limit):
    answer = 0
    people.sort()
    people.reverse()
    check=[0]*(len(people)+1)
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            if (people[i]+people[j])<=limit and check[i]==0 and check[j]==0:
                answer+=1
                check[i]=1
                check[j]=1
    answer+=(check.count(0)-1)
    return answer
'''