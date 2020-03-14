/* 자바스크립트 배열 메소드 */

// [1] concat() : 인자로 주어진 값을 배열에 합쳐서 새 배열을 만든다.
let arr = [1,2,3];
console.log(arr.concat(4,5,6))      // [ 1, 2, 3, 4, 5, 6 ]
console.log(arr.concat([4,5,6]))    // [ 1, 2, 3, 4, 5, 6 ]
console.log(arr.concat(4,5,[6]))    // [ 1, 2, 3, 4, 5, 6 ]
console.log(arr)    // 원본은 바뀌지 않음 : [ 1, 2, 3 ]

// [2] every() : 배열의 모든 원소가 제공한 함수를 통과하는지 테스트하는 메소드
// [2] some() : 배열의 원소중 하나라도 제공한 함수를 통과하는지 테스트하는 메소드
arr = [1,2,3];
console.log(arr.every(el => el%2 === 0));    // false
console.log(arr.some(el => el%2 === 0));     // ture

// [3] fill() : 배열 전체를 특정 값으로 채우는 메소드
arr.fill(5);
console.log(arr)    // 원본이 바뀜 : [ 5, 5, 5 ]


// [4] filter() : 배열의 원소 중 제공된 함수를 통과하는 원소를 반환
arr = [1,2,3,4,5]
console.log(arr.filter(el => el < 3))   // [ 1, 2 ]
console.log(arr)    // 원본은 바뀌지 않음 : [ 1, 2, 3, 4, 5 ]


// [5] forEach() : 배열 원소마다 제공한 함수를 실행하는 메소드
arr = [1,2,3]
arr.forEach(el=>console.log(el))    // 1 2 3
console.log(arr)    // 원본은 바뀌지 않음 : [ 1, 2, 3 ]
arr.forEach((el,index)=>console.log(index+"번째 원소는 "+el))   // index도 넘길 수 있다.


// [6] includes() : 배열에 특정 원소가 포함돼 있는지 여부를 판단하여 true, false 반환
arr = [1,2,3,[4]]
console.log(arr.includes(3))    // true
console.log(arr.includes([4]))     // false : 배열끼리는 같은 주소를 참고하는 것이 아니라면 무조건 false


// [7] indexOf(), lastIndexOf() : 배열에 특정 원소가 포함되어 있는지 여부를 확인
// 원소가 존재하지 않으면 -1 반환
arr = [1,2,3,2] 
console.log(arr.indexOf(2))     // 1
console.log(arr.lastIndexOf(2))     // 3
console.log(arr.indexOf(5))     // -1


// [8] join() : 모든 원소를 연결해 하나의 문자로 만든다.
arr = [1,2,3]
console.log(arr.join())     // 1,2,3
console.log(arr.join(""))     // 123
console.log(arr.join(" / "))     // 1 / 2 / 3


// [9] map() : 배열 내의 모든 원소에 대하여 제공된 함수를 호출하고, 결과를 모아 새로운 배열을 리턴하는 메소드
arr = [1,2,3]
console.log(arr.map(el => el*2))    // [ 2, 4, 6 ]
console.log(arr)    // 원본은 바뀌지 않음 : [ 1, 2, 3 ]


// [10] push() : 배열의 맨 뒤에 원소 추가
// [10] pop() : 배열의 맨 뒤의 원소 삭제
// [10] unshift() : 배열의 맨 앞에 원소 추가
// [10] shift() : 배열의 맨 앞의 원소 삭제
arr = [1,2,3]
console.log(arr.push(4))  // 4
console.log(arr.pop())  // 4
console.log(arr.unshift(4))  // 0
console.log(arr.shift())  // 0


// [11] reduce(), reduceRight() : 배열의 원소마다 누적 계산값과 함께 함수 적용하여 하나의 값으로 리턴
arr = [1,2,3]
console.log(arr.reduce((a,b) => a+b)) // 6
console.log(arr.reduce((a,b) => a+b,10)) // 16
console.log(arr)    // 원본은 바뀌지 않음 : [ 1, 2, 3 ]


// [12] reverse() : 배열의 원소를 뒤집음
arr = [1,2,3]
console.log(arr.reverse())  // [ 3, 2, 1 ]
console.log(arr)    // 원본이 바뀜 : [ 3, 2, 1 ]


// [13] slice(start, end) : 배열의 start부터 end-1까지 shallow copy하는 메소드
arr = [1,2,3]
console.log(arr.slice(1))  //  [ 2, 3 ]
console.log("11",arr.slice(0,1))  //  [ 1 ]
console.log(arr)    // 원본 안바뀜 : [ 1, 2, 3 ]


// [14] splice(start, 삭제할 원소 개수, item1, item2, ...) : 배열의 원소를 start부터 삭제하거나 새로운 원소(item1, item2, ...)를 추가한다.
arr = [1,2,3]
console.log(arr.splice(1))   // 삭제된 배열 리턴 : [ 2, 3 ] - 1번 인덱스부터 끝까지 삭제됨
console.log(arr)    // 원본이 바뀜 : [ 1 ]

arr = [1,2,3]
console.log(arr.splice(1,1))   // 삭제된 배열 리턴 : [ 2 ]
console.log(arr)    // 원본이 바뀜 : [ 1, 3 ]

arr = [1,2,3]
console.log(arr.splice(1,2,4,5))   // 삭제된 배열 리턴 : [ 2, 3 ]
console.log(arr)    // 원본이 바뀜 : [ 1, 4, 5 ]


// [15] sort() : 배열을 정렬하는데 사용, 일반적으로 유니코드 순서대로 정렬
arr = [1,5,6,2,4,3,0]
arr.sort((a,b)=>a-b)   // 오름차순(작(a)=>큰(b))
console.log(arr)    // 원본이 바뀜 : [ 0, 1, 2, 3, 4, 5, 6 ]


// [16] toString() : 배열의 원소를 문자열로 반환
arr = [1,2,3]
console.log(arr.toString())   // 1,2,3
console.log(arr)    // 원본 안바뀜 : [ 1, 2, 3 ]


// [17] from(사용될 유사배열, callback) : 유사 배열을 얕게 복사해 배열로 변환해주는 역할
arr = Array.from("foo")
console.log(arr)    // [ 'f', 'o', 'o' ]
arr = Array.from([1,2,3], (x) => x+x)
console.log(arr)    // [ 2, 4, 6 ]


// [문제 1] i번째 인덱스의 값이 i+1인 길이 10의 배열을 만드시오.
arr = Array(10).fill(null).map((item, index) => index + 1)
console.log(arr)    // [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


// [문제 2] (독립된) 2차원 배열을 만드시오.
// 자바스크립트 다차원 배열 선언 방법(https://smilerici.tistory.com/71)
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