#프로그래머스 모의고사

def solution(answers):
    answer = []
    f_ans=[1,2,3,4,5]
    s_ans=[2,1,2,3,2,4,2,5]
    t_ans=[3,3,1,1,2,2,4,4,5,5]
    score=[0]*(3)
    for i in range(len(answers)):
        if answers[i]==f_ans[i%5]:
            score[0]+=1
        if answers[i]==s_ans[i%8]:
            score[1]+=1
        if answers[i]==t_ans[i%10]:
            score[2]+=1
    M=max(score)
    for i in range(3):
        if score[i]==M:
            answer.append(i+1)
    return answer