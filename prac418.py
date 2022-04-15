# 백준 2270


def hanoi(pillar, pillar_pos):
    if pillar:
        if pillar[1:]:
            return hanoi(pillar[1:], [pillar_pos[0], pillar_pos[2], pillar_pos[1]])+[[pillar_pos[0], pillar_pos[2]]]+hanoi(pillar[1:], [pillar_pos[1], pillar_pos[0], pillar_pos[2]])
        else:
            return [[pillar_pos[0], pillar_pos[2]]]


def solution(n):
    answer = []
    pillar = [i for i in range(n, 0, -1)]
    pillar_pos = [1, 2, 3]
    answer = hanoi(pillar, pillar_pos)
    return answer


n = int(input())
ans = solution(n)
print(len(ans))
for a in ans:
    print(*a)
