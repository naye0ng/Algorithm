"""
큐빙
https://www.acmicpc.net/problem/5373
"""
"""
U: 윗 면, 
D: 아랫 면, 
F: 앞 면, 
B: 뒷 면, 
L: 왼쪽 면, 
R: 오른쪽 면

+: 시계 방향 (그 면을 바라봤을 때가 기준)
-: 반시계 방향
"""
def clockwise(C) :
    temp = [['']*3 for _ in range(3)]
    for x in range(3) :
        for y in range(3) :
            temp[y][3-x-1] = cube[C][x][y]
    cube[C] = temp

def counterclockwise(C) :
    temp = [['']*3 for _ in range(3)]
    for x in range(3):
        for y in range(3):
            temp[3-y-1][x] = cube[C][x][y]
    cube[C] = temp

def U_Plus() :
    clockwise(U)
    cube[L][0], cube[F][0], cube[R][0], cube[B][0] = cube[F][0], cube[R][0], cube[B][0], cube[L][0]

def U_Minus() :
    counterclockwise(U)
    cube[L][0], cube[F][0], cube[R][0], cube[B][0] = cube[B][0], cube[L][0], cube[F][0], cube[R][0]

def D_Plus() :
    clockwise(D)
    cube[L][2], cube[F][2], cube[R][2], cube[B][2] = cube[B][2], cube[L][2], cube[F][2], cube[R][2]

def D_Minus() :
    counterclockwise(D)
    cube[L][2], cube[F][2], cube[R][2], cube[B][2] = cube[F][2], cube[R][2], cube[B][2], cube[L][2]

def F_Plus() :
    clockwise(F)
    temp1, temp2, temp3 = cube[U][2][0], cube[U][2][1], cube[U][2][2]
    cube[R][0][0], cube[R][1][0], cube[R][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[R][0][0], cube[R][1][0], cube[R][2][0]
    cube[D][0][2], cube[D][0][1], cube[D][0][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[D][0][2], cube[D][0][1], cube[D][0][0]
    cube[L][2][2], cube[L][1][2], cube[L][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[L][2][2], cube[L][1][2], cube[L][0][2]
    cube[U][2][0], cube[U][2][1], cube[U][2][2] = temp1, temp2, temp3

def F_Minus() :
    counterclockwise(F)
    temp1, temp2, temp3 = cube[U][2][0], cube[U][2][1], cube[U][2][2]
    cube[L][2][2], cube[L][1][2], cube[L][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[L][2][2], cube[L][1][2], cube[L][0][2]
    cube[D][0][2], cube[D][0][1], cube[D][0][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[D][0][2], cube[D][0][1], cube[D][0][0]
    cube[R][0][0], cube[R][1][0], cube[R][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[R][0][0], cube[R][1][0], cube[R][2][0]
    cube[U][2][0], cube[U][2][1], cube[U][2][2] = temp1, temp2, temp3

def B_Plus():
    clockwise(B)
    temp1, temp2, temp3 = cube[U][0][2], cube[U][0][1], cube[U][0][0]
    cube[L][0][0], cube[L][1][0], cube[L][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[L][0][0], cube[L][1][0], cube[L][2][0]
    cube[D][2][0], cube[D][2][1], cube[D][2][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[D][2][0], cube[D][2][1], cube[D][2][2]
    cube[R][2][2], cube[R][1][2], cube[R][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[R][2][2], cube[R][1][2], cube[R][0][2]
    cube[U][0][2], cube[U][0][1], cube[U][0][0] = temp1, temp2, temp3

def B_Minus():
    counterclockwise(B)
    temp1, temp2, temp3 = cube[U][0][2], cube[U][0][1], cube[U][0][0]
    cube[R][2][2], cube[R][1][2], cube[R][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[R][2][2], cube[R][1][2], cube[R][0][2]
    cube[D][2][0], cube[D][2][1], cube[D][2][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[D][2][0], cube[D][2][1], cube[D][2][2]
    cube[L][0][0], cube[L][1][0], cube[L][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[L][0][0], cube[L][1][0], cube[L][2][0]
    cube[U][0][2], cube[U][0][1], cube[U][0][0] = temp1, temp2, temp3

def L_Plus():
    clockwise(L)
    temp1, temp2, temp3 = cube[U][0][0], cube[U][1][0], cube[U][2][0]
    cube[F][0][0], cube[F][1][0], cube[F][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[F][0][0], cube[F][1][0], cube[F][2][0]
    cube[D][0][0], cube[D][1][0], cube[D][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[D][0][0], cube[D][1][0], cube[D][2][0]
    cube[B][2][2], cube[B][1][2], cube[B][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[B][2][2], cube[B][1][2], cube[B][0][2]
    cube[U][0][0], cube[U][1][0], cube[U][2][0] = temp1, temp2, temp3

def L_Minus():
    counterclockwise(L)
    temp1, temp2, temp3 = cube[U][0][0], cube[U][1][0], cube[U][2][0]
    cube[B][2][2], cube[B][1][2], cube[B][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[B][2][2], cube[B][1][2], cube[B][0][2]
    cube[D][0][0], cube[D][1][0], cube[D][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[D][0][0], cube[D][1][0], cube[D][2][0]
    cube[F][0][0], cube[F][1][0], cube[F][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[F][0][0], cube[F][1][0], cube[F][2][0]
    cube[U][0][0], cube[U][1][0], cube[U][2][0] = temp1, temp2, temp3

def R_Plus():
    clockwise(R)
    temp1, temp2, temp3 = cube[U][2][2], cube[U][1][2], cube[U][0][2]
    cube[B][0][0], cube[B][1][0], cube[B][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[B][0][0], cube[B][1][0], cube[B][2][0]
    cube[D][2][2], cube[D][1][2], cube[D][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[D][2][2], cube[D][1][2], cube[D][0][2]
    cube[F][2][2], cube[F][1][2], cube[F][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[F][2][2], cube[F][1][2], cube[F][0][2]
    cube[U][2][2], cube[U][1][2], cube[U][0][2] = temp1, temp2, temp3

def R_Minus():
    counterclockwise(R)
    temp1, temp2, temp3 = cube[U][2][2], cube[U][1][2], cube[U][0][2]
    cube[F][2][2], cube[F][1][2], cube[F][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[F][2][2], cube[F][1][2], cube[F][0][2]
    cube[D][2][2], cube[D][1][2], cube[D][0][2], temp1, temp2, temp3 = temp1, temp2, temp3, cube[D][2][2], cube[D][1][2], cube[D][0][2]
    cube[B][0][0], cube[B][1][0], cube[B][2][0], temp1, temp2, temp3 = temp1, temp2, temp3, cube[B][0][0], cube[B][1][0], cube[B][2][0]
    cube[U][2][2], cube[U][1][2], cube[U][0][2] = temp1, temp2, temp3

U, D, F, B, L, R = 0, 1, 2, 3, 4, 5
T = int(input())
for _ in range(T) :
    cube = [
        [['w'] * 3 for _ in range(3)],  # 위
        [['y'] * 3 for _ in range(3)],  # 아래
        [['r'] * 3 for _ in range(3)],  # 앞
        [['o'] * 3 for _ in range(3)],  # 뒤
        [['g'] * 3 for _ in range(3)],  # 왼
        [['b'] * 3 for _ in range(3)]  # 오
    ]

    n = int(input())
    for str in input().split() :
        if str == 'U+' :
            U_Plus()
        elif str == 'U-' :
            U_Minus()
        elif str == 'D+' :
            D_Plus()
        elif str == 'D-' :
            D_Minus()
        elif str == 'F+' :
            F_Plus()
        elif str == 'F-' :
            F_Minus()
        elif str == 'B+' :
            B_Plus()
        elif str == 'B-' :
            B_Minus()
        elif str == 'L+' :
            L_Plus()
        elif str == 'L-' :
            L_Minus()
        elif str == 'R+' :
            R_Plus()
        elif str == 'R-' :
            R_Minus()

    for x in range(3) :
        print("".join(cube[0][x]))