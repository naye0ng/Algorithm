// [문제 1] i번째 인덱스의 값이 i+1인 길이 10의 배열을 만드시오.
arr = Array(10).fill(null).map((item, index) => index + 1)
console.log(arr)    // [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


// [문제 2] (독립된) 2차원 배열을 만드시오.
// 자바스크립트 다차원 배열 선언 방법(https://smilerici.tistory.com/71)
// (잘못된 예) - 얕은 복사가 일어남
var array = Array(2).fill([])
array[0][0] = 1
console.log(array)  // [ [ 1 ], [ 1 ] ]


arr = Array(2).fill(null).map(el => [])
arr[0][0] = 1
console.log(arr)

arr = Array.from(Array(2), () => Array())
console.log(arr)    // [ [], [] ]

// [문제 3] [1,2,4,5] 배열의 중간에 3을 삽입하시오.
arr = [1,2,4,5]
arr.splice(2,0,3)   // 2번부터 0개 삭제하고 3을 추가해라
console.log(arr)    // [ 1, 2, 3, 4, 5 ]


// [문제 4] [[1],[2],[3],[4]] 를 deepcopy 하시오.
arr = [[1],[2],[3],[4]]
let copy_arr = JSON.parse(JSON.stringify(arr))
arr[0][0] = 10
console.log(arr)    // [ [ 10 ], [ 2 ], [ 3 ], [ 4 ] ]
console.log(copy_arr)   // [ [ 1 ], [ 2 ], [ 3 ], [ 4 ] ]


// [문제 5] 2차원 배열의 중복을 제거하라.
// 중복 : 길이와 원소들이 같은 것
function getUnique(arr, arrUnique){
    if(arr.length == 0) return arrUnique
    else{
        if(arrUnique.length == 0) arrUnique.push(arr.shift())
        // arr 원소 돌면서 조건에 만족하는 값 뽑아내기
        arr = arr.filter((items)=>{
            isUnique = true
            for(let i = 0; i< arrUnique.length; i++){
                // arrUnique의 원소와 items의 개수가 같다면 원소 비교
                if(arrUnique[i].length == items.length && items.filter(item => arrUnique[i].includes(item)).length == items.length){
                    isUnique = false
                    break
                }
            }
            if(isUnique) arrUnique.push(items)
            return isUnique
        })
        return getUnique(arr, arrUnique)
    }

}
console.log(getUnique([[1],[1,2],[],[],[1],[2],[1]], []))


// [문제 6] 다차원 배열의 빈 배열 제거
arr = [[1],[1,2],[],[],[1],[2],[1]]
console.log(arr.filter(item => item.length > 0))
console.log(arr)


// [문제 7] 1차원 배열의 중복 제거
arr = [1,2,2,2,2,3,4,5,3,4]
console.log(arr.filter((item, index) => {return arr.indexOf(item) == index }))



// [문제 8] : "HELLO HELLO HI HELLO" 에서 모든 HELLO를 HI로 바꿔라
// [문제 9] : [1,2,4,8,16,32] 배열을 만들어라
// [문제 10] : [1,2,3,5,6] splice()를 사용하여 [1,2,3,4,5,6]을 만들어라