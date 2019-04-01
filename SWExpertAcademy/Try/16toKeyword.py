"""
16진수 문자열을 입력받아 암호비트로 표현하시오.
"""
an = input().replace('',' 0x').split(' ')
an = [bin(int(an[i], 16)) for i in range(1,len(an)-1)]

arr =''
for i in range(len(an)) :
    l = an[i][2:]
    for k in range(4-len(l)) :
        arr+='0'
    arr+=l

print(arr)
