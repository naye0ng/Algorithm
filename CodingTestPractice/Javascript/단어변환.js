var answer = 0, visited, L;

// 단어 길이 비교 함수
function compareWords(w1,w2,l,diff){
    if(l==L){
        return true
    }else{
        // 현재 자리 비교하기
        diff += (w1[l] != w2[l])
        if(diff > 1) return false
        return compareWords(w1,w2,l+1,diff)
    }
}

// 단어변환
function changeWord(begin, target, words, count){
    if(begin == target){
        answer = count
    }else if(answer == 0 || answer > count){
        // 변환되지 않은 값 찾아서 타겟으로 변경하기
        for(let i=0;i<words.length;i++){
            // 사용된적 없고, 변환될 수 있다면
            if(visited[i] && compareWords(begin,words[i],0,0)){
                visited[i] -= 1
                changeWord(words[i],target,words,count+1)
                visited[i] += 1
            }
        }
    }
}

function solution(begin, target, words) {
    L = begin.length
    visited = Array(words.length).fill(1);
    changeWord(begin, target, words, 0)
    return answer;
}

