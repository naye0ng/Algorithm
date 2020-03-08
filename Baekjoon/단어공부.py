"""
단어공부
https://www.acmicpc.net/problem/1157
"""
def key_is_value(x) :
    return x[1]

S = input()
alpa = {k:0 for k in range(65, 91)}

"""
[개선점] 아스키 코드로 변환한하고 그냥 "a".upper()하는 방법으로 알파벳 그대로 저장
"""
for i in range(len(S)) :
    if ord(S[i]) >= 65 and ord(S[i]) < 91 :
        alpa[ord(S[i])] += 1
    else :
        alpa[ord(S[i])-32] += 1

values = sorted(alpa.items(), key=key_is_value, reverse=True)

if values[0][1] == values[1][1] :
    print("?")
else :
    print(chr(values[0][0]))