var stop = false;
var answer, visited;

function makePath(tickets,N,n,next_start,result){
    // 알파벳이 빠른것이 먼저 만들어진 경우
    if(!stop){
        if(N == n){
            stop = true;
            // 이거 안하면 answer가 result를 보기 떄문에 문제가 생긴다.
            answer = JSON.parse(JSON.stringify(result))
        }else{
           let i = 0
           while(i<tickets.length){
               // 시작점과 같으면 이동시키기
                if(visited[i] == 0 && next_start == tickets[i][0]){
                    visited[i] = 1
                    result.push(tickets[i][1]);
                    makePath(tickets,N,n+1,tickets[i][1],result)
                    result.pop()
                    visited[i] = 0
                }
                i++
           }
        }
    }
}

function solution(tickets) {
    tickets.sort((a,b)=>{
        // 오름차순 정렬(작 => 큰)
        return a[1] > b[1] || a[0] > b[0]
    });
    visited = Array(tickets.length).fill(0)
    makePath(tickets,tickets.length,0,"ICN", Array("ICN"))
    return answer
}

console.log(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

