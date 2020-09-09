// [문제 1] i번째 인덱스의 값이 i+1인 길이 10의 배열을 만드시오.
arr = Array(10).fill(null).map((value, index) => index+1 )
console.log(arr)    // [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


// [문제 2] (독립된) 2*2차원 배열을 만드시오.
// 자바스크립트 다차원 배열 선언 방법(https://smilerici.tistory.com/71)
// (잘못된 예) - 얕은 복사가 일어남
arr = Array(2).fill(null).map(item => [])
arr[1][0] = 1
console.log(arr)

// [문제 3] [1,2,4,5] 배열의 중간에 3, 3을 삽입하시오.
arr = [1,2,4,5]
arr.splice(arr.length/2, 0, ...[3,3])
console.log(arr)    // [ 1, 2, 3, 3, 4, 5 ]

// [문제 4] [[1],[2],[3],[4]] 를 deepcopy 하시오.
arr = [[1],[2],[3],[4]]
arr2 = JSON.parse(JSON.stringify(arr))
arr2[1][0] = -1
console.log(arr)

// [문제 5] 2차원 배열의 중복을 제거하라.
// 중복 : 길이와 원소들이 같은 것
function getUnique(arr, arrUnique){

}
console.log(getUnique([[1],[1,2],[],[],[1],[2],[1]], []))


// [문제 6] 다차원 배열의 빈 배열 제거
arr = [[1],[1,2],[],[],[1],[2],[1]]


// [문제 7] 1차원 배열의 중복 제거
arr = [1,2,2,2,2,3,4,5,3,4]


// [문제 8] : "HELLO HELLO HI HELLO" 에서 모든 HELLO를 HI로 바꿔라
// [문제 9] : [1,2,4,8,16,32] 배열을 만들어라
arr = Array(6).fill(1)
for(let i in arr){
    v = 1
    if(i > 0) v = arr[i-1]*2
    arr[i] = v
}
console.log(arr)
// [문제 10] : [1,2,3,5,6] splice()를 사용하여 [1,2,3,4,5,6]을 만들어라