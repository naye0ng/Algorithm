// TODO: 2차원 배열 중복 제거
function getUniqueObject(target){

}

function solution(routes) {
    var answer = routes.length, L = routes.length;
    // 자바스크립트 다차원 배열 선언 방법(https://smilerici.tistory.com/71)
    // const array = Array.from(Array(4), () => Array()); 이것도 있음
    let road = Array(60001).fill(null).map(()=> Array())

    for(let i=0;i<L;i++){
        for(let j = routes[i][0]+30000; j <= routes[i][1]+30000; j++){
            road[j].push(i)
        }
    }

    // TODO : 배열 내림차순 나열해봐 ([[1],[],[],[],[1],[2],[1]])
    // 빈값 제거 BUT 배열의 중복 제거는 어려움
    road = road.filter(item => item.length > 0)

    road.sort((a,b)=>{
        // 길이 차이에 의해 sort 해야해
        return b.length - a.length
    })
    
    // 길 한번씩 돌면서 체크
    var visited = Array(L).fill(1)

   
    return answer;
    // 모든 경로 살펴보기
    function makePath(target,n,i){
        if(visited.reduce((a,b)=>a+b) == 0){
            if(answer > n) answer = n;
        }else{
            // i번째꺼 추가하기
        }
    }
}

console.log(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
// console.log(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

/*
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
*/