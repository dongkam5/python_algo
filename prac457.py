# 백준 2470 두 용액
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
i = 0
j = len(lst)-1
answer = [0, 0]
diff = 10**10
while i < j:
    mixed = lst[i]+lst[j]
    if abs(mixed) < diff:
        diff = abs(mixed)
        answer[0] = lst[i]
        answer[1] = lst[j]
        if diff == 0:
            break
    elif mixed > 0:
        j -= 1
    elif mixed < 0:
        i += 1

print(*answer)
