N = int(input())
people = {}
for _ in range(N) :
    k, v = map(int, input().split())
    # 같은시간에 화장실 가는 사람 존재 가능
    if k in people.keys() :
        people[k].append(v-k)
    else :
        people[k] = [v-k]

toilet = [1]
t = 0
while people :
    # 화장실 비우기
    for i in range(len(toilet)) :
        if toilet[i] > 0 :
            toilet[i] -= 1
    # 화장실 가는 사람이 있다면
    if t in people.keys() :
        ends = people.pop(t)
        while ends :
            for i in range(len(toilet)) :
                # 빈 화장실이 있다면 넣기
                if toilet[i] == 0 :
                    toilet[i] = ends.pop(0)
                else :
                    # 없다면 화장실 추가
                    toilet.append(ends.pop(0))
    t += 1
print(len(toilet))

