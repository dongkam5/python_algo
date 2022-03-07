# 백준 11866
N, K = map(int, input().split())
lst = [0]*(N+1)
cnt = 0
k_count = 0
i = 0
answer = []
while N != cnt:
    if lst[i % N+1] == 0:
        k_count += 1
        if k_count == K:
            lst[i % N+1] = 1
            answer.append(i % N+1)
            cnt += 1
            k_count = 0
    i += 1

print('<', end='')
for i in range(len(answer)-1):
    print(str(answer[i])+','+' ', end='')
print(str(answer[-1]), end='')
print('>', end='')
