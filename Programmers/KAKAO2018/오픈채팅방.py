"""
오픈채팅방
"""
# 유저 아이디와 닉네임은 딕셔너리 구성
def solution(records):
    nick = {}
    for recode in records :
        recode = recode.split()
        if recode[0] == "Enter" or recode[0] == "Change" :
            nick[recode[1]] = recode[2]
    answer = []
    for recode in records :
        recode = recode.split()
        if recode[0] == "Enter" :
            answer.append(nick[recode[1]]+"님이 들어왔습니다.")
        elif recode[0] == "Leave" :
            answer.append(nick[recode[1]] + "님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))