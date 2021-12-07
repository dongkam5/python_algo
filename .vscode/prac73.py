#백준 1373
lst=list(map(int,input()))
ans=[]
i=len(lst)-1

while i>=2:
    ans.append(lst[i]+lst[i-1]*2+lst[i-2]*4)
    i-=3

if i==0:
    ans.append(lst[0])
elif i==1:
    ans.append(lst[0]*2+lst[1])

for i in range(len(ans)-1,-1,-1):
    print(ans[i],end='')


#한줄 코드
'''
print(oct(int(input(),2))[2:])
'''

#다른풀이
'''
import sys

x = sys.stdin.readline()
ten_number = 0
answer = ''
for i in range(len(x)):
    ten_number += int(x[-1])*(2**i)
    x = x[:-1]

while ten_number != 0: 
    answer += str(ten_number%8)
    ten_number = ten_number // 8
print(answer[::-1])
'''
