# 백준 9663 N-Queen
def check(n):
    for k in range(n):
        if queen_row[n] == queen_row[k] or abs(queen_row[n]-queen_row[k]) == n-k:
            return False
    return True


def search(n):
    global answer
    if n == N:
        answer += 1
    else:
        for i in range(N):
            queen_row[n] = i
            if check(n):
                search(n+1)


N = int(input())
answer = 0
queen_row = [0]*(N)
search(0)
print(answer)
