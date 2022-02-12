# 백준 2231
n = int(input())
check = 0
for i in range(1, n+1):
    valLst = list(map(int, str(i)))
    val = i+sum(valLst)
    if val == n:
        check = 1
        break
if check:
    print(i)
else:
    print(0)
