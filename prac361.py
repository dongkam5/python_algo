#프로그래머스 [3차] 방금그곡

m_={'C':'a','C#':'b','D':'c','D#':'d','E':'e','E#':'q','F':'f','F#':'g','G':'h','G#':'i','A':'j','A#':'k','B':'l'}
def mel_to_code(melody):
    i=0
    code=[]
    while i<(len(melody)-1):
        if melody[i+1]=='#':
            code.append(m_[melody[i]+melody[i+1]])
            i+=2
        else:
            code.append(m_[melody[i]])
            i+=1
    if not melody[-1]=='#':
        code.append(m_[melody[-1]])
    return code
def solution(m, musicinfos):
    answer =[0,0]
    m=''.join(mel_to_code(m))
    for musicinfo in musicinfos:
        start,end,title,melody=map(str,musicinfo.split(','))
        melody=mel_to_code(melody)
        melody_len=len(melody)
        s_h,s_m=map(int,start.split(':'))
        e_h,e_m=map(int,end.split(':'))
        spend=(e_h-s_h)*60+(e_m-s_m)
        if spend>melody_len:
            for i in range(len(melody),spend):
                melody.append(melody[i%melody_len])
        elif spend<melody_len:
            melody=melody[:spend]
        melody=''.join(melody)
        if m in melody:
            if spend>answer[0]:
                answer[1]=title
                answer[0]=spend
    if answer[1]==0:
        return '(None)'
    else:
        return answer[1]