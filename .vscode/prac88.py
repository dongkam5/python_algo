#백준 1789

n=int(input())

sum=0
i=1
num=0
while n>sum:
    sum+=i
    i+=1
    num+=1

if n==sum:
    print(num)
else:
    print(num-1)