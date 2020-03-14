function solution(land, height) {
    var answer = 0;
    // 상우하좌
    var dx = [-1,0,1,0];
    var dy = [0,1,0,-1];
    var L = land.length;
    var cluster = Array(L).fill(null).map(()=> Array(L).fill(0));
    var group = 1;

    // [1] 이동가능한 그룹 만들기
    for(let x = 0; x < L ; x++){
        for(let y = 0; y < L ; y++){
            if(cluster[x][y] == 0) {
                cluster[x][y] = group
                clustering(x,y)
                group ++
            }
        }
    }
    group--;

    // [2] group이 1개보다 많을때, 모든 그룹이 연결되도록 만들 수 있는 사다리 찾기


    


    if(group > 1) makeBridge()
    return answer

    
    function makeBridge(){
        var visited = Array(group).fill(null).map(()=>Array(group).fill(10000))
        
        for(let x = 0; x < L ; x++){
            for(let y = 0; y < L ; y++){
                for(let i = 0; i < 4; i++){
                    // 상하좌우 살펴서 자신과 다른 그룹이면 사다리 놓을건데, 차이가 작을 수록 좋당
                    if(isNotWall(x+dx[i],y+dy[i]) 
                        && cluster[x][y] != cluster[x+dx[i]][y+dy[i]]){
                            tmp = Math.abs(land[x][y] - land[x+dx[i]][y+dy[i]])
                            A = cluster[x][y]-1, B = cluster[x+dx[i]][y+dy[i]]-1
                            visited[A][B] = Math.min(visited[A][B], tmp)
                            visited[B][A] = Math.min(visited[B][A], tmp)
                    }
                }
            }
        }

        // 전체가 이어져있음을 확인해야한다.
        
    
        for(let x = 0; x < group ; x++){
            for(let y = 0; y < x ; y++){
                if(visited[x][y] < 10000 ){

                }
            }
        }


        // group-1 개 찾기
        // var tmp = []
        // for(let x = 0; x < group ; x++){
        //     for(let y = 0; y < x ; y++){
        //         if(visited[x][y] < 10000){
        //             tmp.push(visited[x][y])
        //         }
        //     }
        // }
        // // 오름차순 정렬(작=>큰)
        // tmp.sort((a,b)=>{
        //     return a-b
        // })
        // answer = tmp.slice(0,group-1).reduce((a,b)=> a+b)
    
    }

    // 이동가능한 그룹 찾기
    function clustering(x,y){
        var queue = []
        queue.push([x,y])
        while(queue.length){
            let q = queue.shift()
            for(let i = 0; i < 4; i++){
                // 벽이 아니고, 다른 그룹에 속해있지 않으면서, 이동이 가능할 경우
                if(isNotWall(q[0]+dx[i],q[1]+dy[i]) 
                    && cluster[q[0]+dx[i]][q[1]+dy[i]] == 0 
                    && Math.abs(land[q[0]][q[1]]-land[q[0]+dx[i]][q[1]+dy[i]]) <= height ){
                        cluster[q[0]+dx[i]][q[1]+dy[i]] = group
                        queue.push([q[0]+dx[i],q[1]+dy[i]])
                    }
            }
        }
    }

    // 범위체크
    function isNotWall(x,y){
        if(x< 0 || x>= L) return false
        if(y< 0 || y>= L) return false
        return true
    }
}

// console.log(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],100))
console.log(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1))
