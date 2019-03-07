"""
2529.부등호
"""
def make(pre, visited, k) :
    global K
    if sum(visited) == K+1 :
        global minV, maxV
        p = int(pre)
        if p < minV :
            minV = p
            result[0] = pre
        if p > maxV :
            maxV = p
            result[1] = pre
        return ""
    for i in range(10) :
        if visited[i] == 1 :
            continue
        localvist = visited[:]
        if kn[k] == "<" and int(pre[-1]) < i:
            localvist[i] = 1
            make(pre+str(i),localvist,k+1)
        elif kn[k] == ">" and int(pre[-1]) > i :
            localvist[i] = 1
            make(pre+str(i),localvist,k+1)

K = int(input())
kn = input().split()


minV = 9999999999
maxV = 0
result = ["",""]
for n in range(10) :
    v = [0] * 10
    v[n] = 1
    make(str(n), v,0)

print(result[1])
print(result[0])
