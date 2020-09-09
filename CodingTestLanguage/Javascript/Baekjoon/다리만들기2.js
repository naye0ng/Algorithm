const readline = require('readline');

(async () => {
    const dx = [-1, 0, 1, 0]
    const dy = [0, 1, 0, -1]
    const is_not_wall = (x, y) => {
        if (x < 0 || x >= N) return false
        if (y < 0 || y >= M) return false
        return true
    }

    const checkIsland = () => {
        const islandPoint = []
        let island = 2
        for (let x = 0; x < N; x++) {
            for (let y = 0; y < M; y++) {
                if (board[x][y] !== 1) continue
                let queue = []
                queue.push([x, y])
                board[x][y] = island
                const point = []
                point.push([x, y])
                while (queue.length) {
                    let [a, b] = queue.shift()
                    for (let i = 0; i < 4; i++) {
                        if (is_not_wall(a + dx[i], b + dy[i]) && board[a + dx[i]][b + dy[i]] == 1) {
                            queue.push([a + dx[i], b + dy[i]])
                            board[a + dx[i]][b + dy[i]] = island
                            point.push([a + dx[i], b + dy[i]])
                        }
                    }
                }
                islandPoint.push(point)
                island++
            }
        }
        makeBridgeList(island - 2, islandPoint)
    }

    const makeBridgeList = (numOfIsland, islandPoint) => {
        const bridge = Array(numOfIsland).fill(null).map(v => Array(numOfIsland).fill(INF))
    
        // i번때 섬에서 j번째 섬으로 가는 가장 짧은 구간
        for (let i = 0; i < numOfIsland - 1; i++) {
            for (let j = i+1; j < numOfIsland; j++) {
                const I = islandPoint[i].length
                const J = islandPoint[j].length
                
                for (let i2 = 0; i2 < I; i2++) {
                    for (let j2 = 0; j2 < J; j2++) {
                        if (islandPoint[i][i2][0] == islandPoint[j][j2][0]) {
                            let bridgeLength = 0
                            let canMakeBridge = true
                            
                            let x = islandPoint[i][i2][0]
                            let [y1, y2] = [islandPoint[i][i2][1], islandPoint[j][j2][1]]

                            if (y1 > y2) [y1, y2] = [y2, y1]
                           
                            for (let y = y1 + 1; y < y2; y++) {
                                if (board[x][y] !== 0) {
                                    canMakeBridge = false
                                    break
                                }
                                bridgeLength++
                            }
                            // [해결] 다리의 길이는 2 이상이어야 한다.
                            if(!canMakeBridge || bridgeLength <= 1) continue
                            
                            bridge[i][j] = Math.min(bridge[i][j], bridgeLength)
                            bridge[j][i] = Math.min(bridge[j][i], bridgeLength)

                        } 
                        else if (islandPoint[i][i2][1] == islandPoint[j][j2][1]) {
                            let bridgeLength = 0
                            let canMakeBridge = true

                            let y = islandPoint[i][i2][1]
                            let [x1, x2] = [islandPoint[i][i2][0], islandPoint[j][j2][0]]
                            if (x1 > x2) [x1,x2] = [x2, x1]

                            for (let x = x1 + 1; x < x2; x++) {
                                if (board[x][y] !== 0) {
                                    canMakeBridge = false
                                    break
                                }
                                bridgeLength++
                            }

                            if(!canMakeBridge || bridgeLength <= 1) continue

                            bridge[i][j] = Math.min(bridge[i][j], bridgeLength)
                            bridge[j][i] = Math.min(bridge[j][i], bridgeLength)

                        }
                    }
                }
            }
        }
        // 가장 작은 값 찾기
        chooseMinBridge(bridge)
    }

    const chooseMinBridge = (bridge) => {
        const B = bridge.length
        const visited = Array(B).fill(false)
        // 방문한적 있는 점들 중, 가장 작은값 선택하기
        const connectedBridge = [0]
        visited[0] = true

        let lengthOfBridges = 0
        while(true){
            let minLength = INF
            let newBridge = -1
            for(let oldBridge of connectedBridge){
                
                // 연결된적 없는 제일 작은 값 찾기
                bridge[oldBridge].forEach((value, index) => {
                    if(!visited[index] && value < minLength) {
                        newBridge = index
                        minLength = value
                        return value
                    }
                    return minLength
                })
            }

            if(newBridge == -1){
                lengthOfBridges = -1
                break
            }

            lengthOfBridges += minLength
            visited[newBridge] = true
            connectedBridge.push(newBridge)
            if(!visited.includes(false)){
                break
            }
        }

        
        console.log(lengthOfBridges)
    }

    let rl = readline.createInterface({ input: process.stdin })
    let N = -1
    let M = -1
    let board = []
    let INF = 0

    for await (const line of rl) {
        if (N == -1) {
            [N, M] = line.split(' ').map(v => v * 1)
            INF = N >= M ? N + 1 : M + 1
            continue
        }
        board.push(line.split(' ').map(v => v * 1))
        // if (board.length == N) rl.close();
    }
    checkIsland()
    rl.close();
    process.exit();
})();
