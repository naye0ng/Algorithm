sn= input()

# 문자열 탐색
alpa = []
i = 0 
while i < len(sn) :
    # 대문자라면
    if ord(sn[i]) >=65 and ord(sn[i]) <=90 :
        s = sn[i]
        i+=1
        # 뒤에 소문자 탐색
        while i :
            # 다음 글자가 소문자라면
            if ord(sn[i]) >=97 and ord(sn[i]) <= 122 :
                s+=sn[i]
                i+=1
            else :
                break
        alpa.append(s)
    else :
        # 숫자가 나온다면 
        break

N = len(alpa)
if  len(sn[i:]) != N :
    print('error')
else :
    result = ''
    for i in range(N) :
        if sn[N+i] == '1' :
            result+=alpa[i]
        else :
            result+=alpa[i]+sn[N+i]
    print(result)


