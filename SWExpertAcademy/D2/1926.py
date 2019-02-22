"""
1926.간단한 369게임
"""
n = int(input())
stran = [str(i) for i in range (1,n+1)]

# for i in range(n) :
#     k = 0
#     if '3' in stran[i] :
#         k+=1
#     if '6' in stran[i] :
#         k+=1
#     if '9' in stran[i] :
#         k+=1
#     if k != 0 :
#         stran[i] = "-"*k

for i in range(n) :

    k = stran[i].count('3') + stran[i].count('6') +stran[i].count('9')
    if k != 0 :
        stran[i] = "-"*k


        
print(" ".join(stran))