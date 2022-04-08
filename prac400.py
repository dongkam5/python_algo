# 프로그래머스 베스트앨범

def solution(genres, plays):
    answer = []
    genre_ = set(genres)
    sum_play = {}
    lst = {}
    for genre in genre_:
        lst[genre] = []
        sum_play[genre] = 0
    for val in enumerate(zip(genres, plays)):
        lst[val[1][0]].append([val[0], val[1][1]])
        sum_play[val[1][0]] += val[1][1]
    sum_play = sorted(sum_play.items(), key=lambda x: -x[1])
    for genre in genre_:
        lst[genre] = sorted(lst[genre], key=lambda x: -x[1])
    for genre, S in sum_play:
        if len(lst[genre]) >= 2:
            answer.append(lst[genre][0][0])
            answer.append(lst[genre][1][0])
        elif len(lst[genre]) == 1:
            answer.append(lst[genre][0][0])
    return answer


print(solution(["classic", "pop", "classic",
      "classic", "pop"], [500, 600, 150, 800, 2500]))
