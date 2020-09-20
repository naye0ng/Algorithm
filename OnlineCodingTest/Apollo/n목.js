function is_not_wall(h, w, x, y){
    if(x < 0 || x >= h) return false
    if(y < 0 || y >= w) return false
    return true
}

function row(h, w, n, board){
    let count = 0
    for(let x = 0; x < h; x++){
        let start = false
        let local_n = 0
        let y = 0
        while(y < w){
            if(board[x][y]){
                if(!start) start = true
                local_n += 1
            }else if(!board[x][y] && start){
                if(local_n == n) count += 1
                local_n = 0
                start = false
            }
            y += 1
        }
        if(local_n == n) count += 1
    }
    return count
}

function column(h, w, n, board){
    let count = 0
    for(let y = 0; y < w; y++){
        let start = false
        let local_n = 0
        let x = 0
        while(x < h){
            if(board[x][y]){
                if(!start) start = true
                local_n += 1
            }else if(!board[x][y] && start){
                if(local_n == n) count += 1
                local_n = 0
                start = false
            }
            x += 1
        }
        if(local_n == n) count += 1
    }
    return count
}

function diagonal_right(h, w, n, board){
    let visited = Array(h).fill(null).map(v => new Array(w).fill(false))
    let count = 0
    for(let x = 0; x < h-n+1; x++){
        for(let y = 0; y < w-n+1; y++){
            if(board[x][y] && !visited[x][y]){
                let local_n = 0
                let [a, b] = [x, y]
                while(is_not_wall(h, w, a, b)){
                    if(!board[a][b]) break
                    local_n += 1
                    visited[a][b] = true
                    a += 1
                    b += 1
                }
                if(local_n == n) count += 1
            }
        }
    }
    return count
}

function diagonal_left(h, w, n, board){
    let visited = Array(h).fill(null).map(v => new Array(w).fill(false))
    let count = 0
    for(let x = 0; x < h-n+1; x++){
        for(let y = w-1; y >= n-1; y--){
            if(board[x][y] && !visited[x][y]){
                let local_n = 0
                let [a, b] = [x, y]
                while(is_not_wall(h, w, a, b)){
                    if(!board[a][b]) break
                    local_n += 1
                    visited[a][b] = true
                    a += 1
                    b -= 1
                }
                if(local_n == n) count += 1
            }
        }
    }
    return count
}

function solution(h, w, n, board) {
    board = board.map(str => str.split('').map(v => v*1))
    return row(h, w, n, board) + column(h, w, n, board) + diagonal_right(h, w, n, board) +diagonal_left(h, w, n, board)
}

console.log(solution(5, 5, 5, ["11111", "11111", "11111", "11111", "11111"]))

