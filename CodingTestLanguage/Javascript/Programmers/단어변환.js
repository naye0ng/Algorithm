function diffOne(str1, str2){
    let diff = 0
    for(let i = 0; i< str1.length; i++){
        if(str1[i] !== str2[i]) diff++
    }
    if(diff === 1) return true
    return false
}

function DFS(begin, target, words, depth){
    if(begin === target){
        answer = Math.min(answer, depth)
    }else if(depth < answer){
        for(let i = 0; i< words.length; i++){
            if(!visited[i] && diffOne(begin, words[i])){
                visited[i] = true
                DFS(words[i], target, words, depth+1)
                visited[i] = false
            }
        }
    }
}

let answer = 0
let visited = []
function solution(begin, target, words) {
    if(!words.includes(target)) return answer

    answer = words.length;
    visited = Array(answer).fill(false)
    DFS(begin, target, words, 0)
    return answer;
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

