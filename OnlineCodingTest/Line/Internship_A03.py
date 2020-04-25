# 입력
N1 = int(input())
# 헤더
header1 = input().split()
table1 = []
for i in range(N1-1) :
    t = input().split()
    table1.append(t)
table1.sort()

N2 = int(input())
header2 = input().split()

table2 = []
for i in range(N2-1) :
    t = input().split()
    table2.append(t)
table2.sort()

h1 = len(header1)
h2 = len(header2)
for y1 in range(h1) :
    print(header1[y1], end=' ')
for y2 in range(1,h2) :
    print(header2[y2], end=' ')
print()
p2 = 0
for x in range(N1-1) :
    # table1
    for y1 in range(h1) :
        print(table1[x][y1], end=' ')
    # table2
    if table1[x][0] == table2[p2][0] :
        for y2 in range(1,h2) :
            print(table2[p2][y2], end=' ')
        if p2 < N2-2 :
            p2+=1
    else :
        print('NULL '*(h2-1), end=' ')
    
    print()
    
    

    
'''
6
id name occupation
5 Brown Accountant
2 Cony Programmer
3 Sally Doctor
1 James Singer
4 Moon Dancer
7
id city zip
2 Seoul 10008
7 Busan 40002
5 Gwangju 20009
6 Daegu 30008
3 Seoul 40005
1 Seoul 50006
'''
