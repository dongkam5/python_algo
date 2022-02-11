# 백준 2467
n = int(input())
lst = list(map(int, input().split()))
val = 10000000000
answer = [0, 0]
i = 0
j = len(lst)-1
while i < j:
    if lst[j]+lst[i] < 0:
        if val > abs(lst[i]+lst[j]):
            val = abs(lst[i]+lst[j])
            answer[0] = lst[i]
            answer[1] = lst[j]
        i += 1
    elif lst[j]+lst[i] > 0:
        if val > abs(lst[i]+lst[j]):
            val = abs(lst[i]+lst[j])
            answer[0] = lst[i]
            answer[1] = lst[j]
        j -= 1
    else:
        answer[0] = lst[i]
        answer[1] = lst[j]
        break

print(answer[0], answer[1])
