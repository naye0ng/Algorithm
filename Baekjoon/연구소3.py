"""
연구소
https://www.acmicpc.net/group/practice/7266/5
"""
from collections import deque 

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

# [3] 모두 다 활성화 됐는지 체크
def mission_success(visited) :
    is_success = True
    for x in range(N) :
        for y in range(N) :
            """
            [주의3] 
            - 남은 값이 그냥 바이러스면 굳이 방문 안해도 됨!
            - 가보지 않았더라도 벽이면 상관 없음
            """
            # 즉, 방문한 적이 없는데, 빈 공간인 경우에만 해당
            if not visited[x][y] and lab[x][y] == 0:
                is_success = False
                break
        if not is_success : 
            break
    return is_success

# [2] 바이러스 활성화
def activate_virus(index) :
    global T
    visited = [[0]*N for _ in range(N)]
    queue = deque([])
    item_cnt = 0
    # virus 자리는 visited 해주고, queue애 담기
    for i in index :
        queue.append(virus[i])
        visited[virus[i][0]][virus[i][1]]
        item_cnt += 1
    """ 
    [주의1] 
    - 바이러스 위치 주의, 아래의 경우 못가는 곳이 생김
        2 0  
        0 2 
    """
    t = 0
    while queue and t < T :
        is_first_change = True
        for _ in range(len(queue)) :
            x, y = queue.popleft()
            for i in range(4) :
                # 바이러스가 퍼질 수 있다면 
                if is_not_wall(x+dx[i], y+dy[i]) and not visited[x+dx[i]][y+dy[i]] :
                    # 벽일 경우에도 True 해줘야 무한루프 안돔
                    
                    visited[x+dx[i]][y+dy[i]] = 1
                    if lab[x+dx[i]][y+dy[i]] != 1 :
                        """ 
                        [주의2]
                        - 퍼지는 것이 있을때만 t를 증가
                        - 이렇게 안하면 마지막에 두번 카운트 됨
                        """
                        if is_first_change :
                            t += 1
                            is_first_change = False
                        queue.append([x+dx[i], y+dy[i]])
                        item_cnt += 1
        """
        [핵심]
        1) 모든 0과 2로 이뤄진 칸을 방문하는 경우
        2) 모든 0과 2를 방문하지 않아도 되는 경우!
            0 0 0 2                       1 1 1 0
            0 2 0 1 이고 2초 뒤에는 visited가 1 1 1 1 가 된다.
            0 0 0 2                       1 1 1 0 
            그러나 (0, 3), (2, 3)의 값은 2로 방문하지 않아도 바이러스가 있는 칸이 된다.
            즉, 바이러스로 가득찰 최소 칸 수는 
            time_limit(0과 2의 개수 = 11) - item_cnt(방문한 0과 2칸의 개수 = 9) <= len(virus) - M : visited 처리되지 않은 2의 수
        """
        if item_cnt >= (time_limit - (len(virus)-M)) and mission_success(visited) :
            T = t
            break

# [1] 바이러스 M개 뽑기
def get_virus(k, m, index) :
    if m == M :
        activate_virus(index)
    else :
        for i in range(k, len(virus)) :
            get_virus(i+1, m+1, index+[i])
    

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus = deque([])

"""
[주의4] 바이러스가 처음부터 다 퍼져있는 경우
"""
time_limit = 0
is_success = True
for x in range(N) :
    for y in range(N) :
        if lab[x][y] == 0 :
            is_success = False
        if lab[x][y] == 2 :
            virus.append([x,y])
        if lab[x][y] != 1: 
            # 0이거나 2이면 이동 가능
            time_limit += 1
"""
[주의5] 최대 N*N번, 최소 (0과 2칸 수 만큼)이동 가능하다
"""
T = time_limit
if is_success : print(0)
else :
    get_virus(0,0,[])
    if T == time_limit : print(-1)
    else : print(T)