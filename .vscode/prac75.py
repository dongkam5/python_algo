#백준 1373

x =list(map(int,input()))
ten_number = 0
answer = ''
for i in range(len(x)):
    ten_number += x[-1]*(2**i)
    x = x[:-1]

while ten_number != 0: 
    answer += str(ten_number%8)
    ten_number = ten_number // 8
print(answer[::-1])