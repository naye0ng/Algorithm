M, N = map(int, input().split())

arr = [0 for _ in range(M,N+1)]
min_value, sum_value = 10001, 0
for i in range(1,N+1) :
    if i*i > N :
        break
    if i*i < M :
        continue
    min_value = min(min_value, i*i)
    sum_value += i*i

print(min_value, sum_value)