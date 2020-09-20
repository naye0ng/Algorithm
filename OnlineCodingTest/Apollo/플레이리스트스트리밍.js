// function solution(play_list, listen_time) {
//     if(play_list.reduce((a,b) => a+b) <= listen_time) return play_list.length
//     const limit = play_list.length
//     play_list = play_list.concat(play_list)
    
//     let answer = 0
//     let [time, count] = [1,1]
//     for(let i = 1; i< play_list.length; i++){
//         time += play_list[i]
//         count += 1
//         if(time >= listen_time || count == limit){
//             answer = Math.max(answer, count)
//             time = 1
//             count = 1
//         }
//     }
//     return answer
// }


function solution(play_list, listen_time) {
    if(play_list.reduce((a,b) => a+b) <= listen_time) return play_list.length
    const music = play_list.length
    play_list = play_list.concat(play_list)

    let count = 0
    for(let start = 0; start < music; start++){
        let [local_count, time] = [1,1]
        let next = start+1
        while(next < play_list.length && time < listen_time && local_count < music){
            time += play_list[next]
            local_count += 1
            next += 1
        }
        count = Math.max(count, local_count)
    }
    return count
}

console.log(solution([1,1,1,5], 5))