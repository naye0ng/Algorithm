m, n = map(int, input().strip().split(' '))
msg = [ int(input()) for _ in range(m)]
consumer = [1 for _ in range(n)]

t = 0
while msg :
    for i in range(n) :
        if consumer[i] == 1 : 
            consumer[i] = msg.pop(0)
        else :
            consumer[i] -= 1
    t += 1
print(t+max(consumer)-1)