"""
2309.일곱 난쟁이
"""
n = 9
people = [ int(input()) for _ in range(n)]

breakPT = False
for i in range(2 << n) :
    if breakPT :
        break
    sum100 = 0
    select = []
    for j in range(n) :
        if i & (1 << j) :
            sum100 += people[j]
            select.append(people[j])
        
        if sum100 == 100 and len(select) == 7:
            breakPT = True
            select.sort()
            for s in select :
                print(s)
            break
        if sum100 >= 100 :
            break
