'''
원자소멸시뮬레이션
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo&categoryId=AWXRFInKex8DFAUo&categoryType=CODE
'''
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def over_board(x, y) :
    if x < 0 or x >= 4001 : return True
    if y < 0 or y >= 4001 : return True
    return False

# [주의] baord가 for문 안에 있다면, 매번 4001*4001의 배열을 생성하므로 런타임에러가 발생한다.
board = [[-1]*4001 for _ in range(4001)]
T = int(input())
for test_case in range(1, 1+T) :
    N = int(input())
    '''
    [런타임 에러]
    board = [[-1]*4001 for _ in range(4001)]
    '''
    atom = []
    for _ in range(N) :
        x, y, d, k = map(int, input().split())
        atom.append([2000+x*2, 2000+y*2, d, k])

    energy = 0
    while atom :
        crush = set()
        next_atom = []
        for _ in range(len(atom)) :
            x, y, d, k = atom.pop(0)
            x += dx[d]
            y += dy[d]

            if over_board(x, y) : continue

            if board[x][y] != -1 :
                crush.add(board[x][y])
                energy += k
                continue

            board[x][y] = len(next_atom)
            next_atom.append([x, y, d, k])
            
        for i in sorted(list(crush), reverse = True) :
            x, y, d, k = next_atom.pop(i)
            board[x][y] = -1
            energy += k

        for i in range(len(next_atom)) :
            x, y, d, k = next_atom[i]
            board[x][y] = -1

        atom = next_atom
            
    print('#{} {}'.format(test_case, energy))

