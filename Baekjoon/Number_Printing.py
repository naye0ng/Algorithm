"""
Number Printing
0 ~ 9의 숫자를 크기와 정렬 방식을 달리하여 인쇄하는 프로그램을 만들고자 한다.

[ 입력 형식 ] 
첫 번째 줄에는 입력 받을 데이터의 갯수와 정렬 방식을 나타내는 값이 공백으로 구분되어 적혀 있다
입력 받을 데이터 개수는 1 <= N <= 100 사이이다
정렬 방식을 나타내는 값은 TOP, BOTTOM 또는 MIDDLE 중 하나이다
TOP은 위 정렬, BOTTOM은 아래 정렬, 그리고 MIDDLE은 중앙 정렬을 의미 한다
두 번째 줄부터 N개의 줄은 크기 숫자들 형식으로 입력된다
크기는 출력할 숫자의 가로 크기를 의미하며 3 이상의 홀수이다
숫자들은 출력 해야 할 숫자열을 의미한다
출력 형식
숫자를 표시하는 부분은 # 문자, 여백을 표시하는 부분은 . 문자를 이용하도록 한다
숫자의 가로 크기는 입력으로 받은 값이다
숫자는 반드시 . 문자를 포함한 크기여야 한다
아래 예시의 숫자 1 또는 6을 보면, 해당 숫자는 . 문자 포함하여 가로 크기가 3이다
숫자의 세로 크기는 입력 받은 가로 크기의 값 중 제일 큰 값을 이용하여 계산한다
제일 큰 값이 n이라 할 때, 2n-1 이다 (제일 큰 가로 크기가 5일 경우 세로 크기는 9)
출력할 숫자 사이에는 한 칸의 공백을 둔다
출력할 숫자는 가로 크기가 3인 경우 아래와 같은 모양이 되도록 한다
### ..# ### ### #.# ### #.. ### ### ###
#.# ..# ..# ..# #.# #.. #.. ..# #.# #.#
#.# ..# ### ### ### ### ### ..# ### ###
#.# ..# #.. ..# ..# ..# #.# ..# #.# ..#
### ..# ### ### ..# ### ### ..# ### ..#

[입력]
4 TOP
5 123
3 45
5 7890
3 6

[출력]
....# ##### ##### #.# ### ##### ##### ##### ##### #..
....# ....# ....# #.# #.. ....# #...# #...# #...# #..
....# ....# ....# ### ### ....# #...# #...# #...# ###
....# ....# ....# ..# ..# ....# #...# #...# #...# #.#
....# ##### ##### ..# ### ....# ##### ##### #...# ###
....# #.... ....# ... ... ....# #...# ....# #...# ...
....# #.... ....# ... ... ....# #...# ....# #...# ...
....# #.... ....# ... ... ....# #...# ....# #...# ...
....# ##### ##### ... ... ....# ##### ....# ##### ...
"""
def print_0(nth, x, w, h) :
    for dx in range(h) :
        board[nth][x+dx][0], board[nth][x+dx][-1] = "#", "#"
    for dy in range(w) :
        board[nth][x][dy], board[nth][x+h-1][dy] = "#", "#"

def print_1(nth, x, w, h) :
    for dx in range(h) :
        board[nth][x+dx][-1] = "#"

def print_2(nth, x, w, h):
    # 세로
    for dx in range(h) :
        if dx < (h//2) :
            board[nth][x+dx][-1] =  "#"
        elif dx > (h//2) :
            board[nth][x+dx][0] =  "#"
    # 가로
    for dy in range(w) :
        board[nth][x][dy], board[nth][h//2+x][dy], board[nth][x+h-1][dy] = "#", "#", "#"

def print_3(nth, x, w, h) :
    for dx in range(h) :
            board[nth][x+dx][-1] =  "#"
    for dy in range(w) :
        board[nth][x][dy], board[nth][h//2+x][dy], board[nth][x+h-1][dy] = "#", "#", "#"

def print_4(nth, x, w, h) :
    for dx in range(h) :
        if dx < (h//2) :
            board[nth][x+dx][0] =  "#"
        board[nth][x+dx][-1] =  "#"
    for dy in range(w) :
        board[nth][h//2+x][dy] = "#"

def print_5(nth, x, w, h) :
    for dx in range(h) :
        if dx < (h//2) :
            board[nth][x+dx][0] =  "#"
        elif dx > (h//2) :
            board[nth][x+dx][-1] =  "#"
    for dy in range(w) :
        board[nth][x][dy], board[nth][h//2+x][dy], board[nth][x+h-1][dy] = "#", "#", "#"

def print_6(nth, x, w, h):
    for dx in range(h) :
        if dx > (h//2) :
            board[nth][x+dx][-1] =  "#"
        board[nth][x+dx][0] =  "#"
    for dy in range(w) :
        board[nth][h//2+x][dy], board[nth][x+h-1][dy] = "#", "#"

def print_7(nth, x, w, h) :
    for dx in range(h) :
        board[nth][x+dx][-1] = "#"
    for dy in range(w) :
        board[nth][x][dy] = "#"    

def print_8(nth, x, w, h) :
    for dx in range(h) :
        board[nth][x+dx][0], board[nth][x+dx][-1] = "#", "#"
    for dy in range(w) :
        board[nth][x][dy], board[nth][h//2+x][dy], board[nth][x+h-1][dy] = "#", "#", "#"

def print_9(nth, x, w, h):
    for dx in range(h) :
        if dx < (h//2) :
            board[nth][x+dx][0] =  "#"
        board[nth][x+dx][-1] = "#"
    for dy in range(w) :
        board[nth][x][dy], board[nth][h//2+x][dy] = "#", "#"
   

N, D = input().split()
N = int(N)

width = []
number = []

for _ in range(N) :
    w, num = input().split()
    for i in range(len(num)) :
        width.append(int(w))
        number.append(int(num[i]))
height = max(width)*2-1
board = [ [["."]*width[i] for _ in range(height)] for i in range(len(number))]

for i in range(len(number)) :
    x, w, h = 0, width[i], width[i]*2-1

    if D == "MIDDLE" :
        x = (height-h)//2
    elif D == "BOTTOM" :
        x = height-h

    if number[i] == 0 :
        print_0(i, x, w, h)
    elif number[i] == 1 :
        print_1(i, x, w, h)  
    elif number[i] == 2 :
        print_2(i, x, w, h) 
    elif number[i] == 3 :
        print_3(i, x, w, h)  
    elif number[i] == 4 :
        print_4(i, x, w, h) 
    elif number[i] == 5 :
        print_5(i, x, w, h)  
    elif number[i] == 6 :
        print_6(i, x, w, h) 
    elif number[i] == 7 :
        print_7(i, x, w, h)  
    elif number[i] == 8 :
        print_8(i, x, w, h)
    elif number[i] == 9 :
        print_9(i, x, w, h)  

for h in range(height) :
    for n in range(len(number)) :
        print("".join(board[n][h]), end=" ")
    print()


"""
4 MIDDLE
3 123
5 45
3 7890
5 6
"""