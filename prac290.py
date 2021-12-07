#프로그래머스 큰 수 만들기 못품
def solution(number, k):
    answer=''
    ind=0
    leng=len(number)
    nums=list(map(int,number))
    nums=nums[:k+1]
    M=max(nums)
    ind=nums.index(M)+1
    answer+=str(M)
    for i in range(1,leng-k):
        nums.append(int(number[k+i]))
        nums=nums[ind:]
        M=max(nums)
        ind=nums.index(M)+1
        answer+=(str(M))
    return answer

n,k=map(int,input().split())
number=input()
print(solution(number,k))