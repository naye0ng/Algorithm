function makeSchedule(jobs){
    const N = jobs.length
    const visited = Array(N).fill(false)
    const poped = Array(N).fill(false)
    
    const heap = []
    let schedule = 0
    let T = 0
    while(visited.includes(false)){
        // 힙에 삽입[i, start, end]
        for(let i=0; i< N; i++){
            let [start, end] = jobs[i]
            if(!poped[i] && start <= T){
                heap.push([i, start, end])
                poped[i] = true
            }
        }

        // 제일 먼저 끝나는 값 찾기
        if(heap.length >= 1){
            heap.sort((job1, job2)=> job1[2] - job2[2])
            const [index, start, end] = heap.shift()   
            visited[index] = true       
            schedule += (T-start)+end
            T += end
        }else{
            T++
        }
    }
    return parseInt(schedule/N)
}

function solution(jobs) {
    return makeSchedule(jobs)
}


// console.log(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))

console.log(solution([[0, 3], [1, 9], [2, 6]]))


