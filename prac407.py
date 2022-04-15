# 프로그래머스 불량 사용자

import math
from itertools import combinations
from collections import defaultdict


def solution(user_id, banned_id):
    answer = 1
    user_id.sort()
    banned_id.sort()
    ban = defaultdict(list)
    ban_id_cnt = defaultdict(int)
    for bid in banned_id:
        for id in user_id:
            if len(id) == len(bid):
                i = 0
                while i < len(id):
                    if bid[i] == '*':
                        i += 1
                        continue
                    if id[i] == bid[i]:
                        i += 1
                    else:
                        break
                if i == len(bid) and id not in ban[bid]:
                    ban[bid].append(id)
    for bid in banned_id:
        ban_id_cnt[bid] += 1
    for bid in ban_id_cnt:
        use = []
        while ban_id_cnt[bid] >= 1:
            for ban_id in ban[bid]:
                if ban_id not in use:
                    use.append(ban_id)
                    ban_id_cnt[bid] -= 1
        if len(use) == len(ban):
            answer += 1
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
      ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
      ["fr*d*", "*rodo", "******", "******"]))
