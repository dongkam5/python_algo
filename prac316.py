#프로그래머스 스킬트리

def solution(skill, skill_trees):
    answer = 0
    skill=list(map(str,skill))
    for skill_tree in skill_trees:
        i=0
        j=0
        check=0
        while i<len(skill_tree) and j<len(skill):
            if skill_tree[i] in skill:
                if skill_tree[i]==skill[j]:
                    j+=1
                    i+=1
                else:
                    check=1
                    break
            else:
                i+=1
        if check!=1:
            answer+=1
    return answer

print(solution('CBD',['BACDE']))