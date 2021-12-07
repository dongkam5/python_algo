#프로그래머스 소수 만들기
def solution(nums):
    def is_prime(n):
        check=0
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                check=1
        if check==0:
            return True
        else:
            return False
    answer = 0
    l=len(nums)
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if is_prime(nums[i]+nums[j]+nums[k]):
                    answer+=1

    return answer