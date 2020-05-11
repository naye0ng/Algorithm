function solution(arr) {
    var array = arr.map(el => (""+el).split("").sort().join(""))
    return array.filter((item, index)=> { return array.indexOf(item) == index}).length
}

// 입력 : [112, 1814, 121, 1481, 1184]
// 답 : 2 

// (문제) 애너그램 겹치는 게 없다면 n^2으로 백만번 돌게됨 >> 터짐 >> 카운팅 정렬?
