#프로그래머스 level2 순위 검색 오답
from collections import defaultdict
def solution(infos, query):
    langs={'cpp':['cpp'],'java':['java'],'python':['python'],'-':['cpp','java','python']}
    postions={'backend':['backend'],'frontend':['frontend'],'-':['backend','frontend']}
    careers={'junior':['junior'],'senior':['senior'],'-':['junior','senior']}
    foods={'chicken':['chicken'],'pizza':['pizza'],'-':['chicken','pizza']}
    answer = []
    dic=defaultdict(dict)
    for info in infos:
        lang,pos,car,food,score=map(str,info.split())
        if dic[lang+pos+car+food].get(score):
            dic[lang+pos+car+food][score]+=1
        else:
            dic[lang+pos+car+food][score]=1
    for q in query:
        temp=0
        lang,pos,car,food_score=map(str,q.split(' and '))
        food,score=map(str,food_score.split())
        for lang_ in langs[lang]:
            for pos_ in postions[pos]:
                for car_ in careers[car]:
                    for food_ in foods[food]:
                        for score_ in dic[lang_+pos_+car_+food_].keys():
                            if int(score_)>=int(score):
                                temp+=dic[lang_+pos_+car_+food_][score_]
        answer.append(temp) 

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


'''
#프로그래머스 level2 순위 검색
from collections import defaultdict
def solution(infos, query):
    langs={'cpp':['cpp','-'],'java':['java','-'],'python':['python','-']}
    postions={'backend':['backend','-'],'frontend':['frontend','-']}
    careers={'junior':['junior','-'],'senior':['senior','-']}
    foods={'chicken':['chicken','-'],'pizza':['pizza','-']}
    answer = []
    dic=defaultdict(dict)
    for info in infos:
        lang,pos,car,food,score=map(str,info.split())
        for lang_ in langs[lang]:
            for pos_ in postions[pos]:
                for car_ in careers[car]:
                    for food_ in foods[food]:
                        if dic[lang_+pos_+car_+food_].get(score):def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer
                            dic[lang_+pos_+car_+food_][score]+=1
                        else:
                            dic[lang_+pos_+car_+food_][score]=1
    for q in query:
        cnt=0
        lang,pos,car,food_score=map(str,q.split(' and '))
        food,score=map(str,food_score.split())
        for score_ in dic[lang+pos+car+food]:
            if int(score_)>=int(score):
                cnt+=dic[lang+pos+car+food][score_]
        answer.append(cnt) 

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
'''