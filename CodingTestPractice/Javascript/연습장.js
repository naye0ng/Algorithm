// 우아한테크캠프 코딩테스트 대비

/******** 1. 문자열 메소드 연습 ********/
var string = "javascript"

// 1-1. 인덱스로 문자열 접근
console.log(string[1])  // a
console.log(string.charAt(1))   // a

// 1-2. 문자열에서 타켓문자의 위치 찾기 - indexOf(), astIndexOf()
console.log("앞에서부터 a 찾기:", string.indexOf('a'))   // 앞에서부터 a 찾기: 1
console.log("뒤에서부터 a 찾기:", string.lastIndexOf('a'))   // 뒤에서부터 a 찾기: 3
console.log("문자열이 없다면?", string.indexOf('k'))    // 문자열이 없다면? -1

// 1-3. 문자열의 문자 바꾸기 - replace(찾을문자,바꿀문자)
string[0] = "J"
console.log(string)    // javascript
string.replace("j", "J")
console.log(string)    // javascript

console.log(string.replace("j", "J"))   // Javascript
string = string.replace("j", "J")
console.log(string)     // Javascript
    // [정리] 자바스크립트에서 문자열은 변경불가! 즉, 재할당을 해주는 방법뿐이다.
console.log(string.replace("a", "A"))   // JAvascript
    // [추가] a가 두개 있지만, 처음 찾은 a만 변경된다.

// 1-4. 문자열 일부 반환 - substring(시작인덱스, 끝날인덱스), substr(시작인덱스, 가져올 문자 개수)
console.log(string.substring(0,4))  // Java
console.log(string.substr(4,6))     // script

// 1-5. 문자열을 자르고 배열로 반환 - split(자를 문자열)
console.log(string.split("a"))  // [ 'J', 'v', 'script' ]

// 1-6. 대소문자 변경
console.log(string.toLowerCase())   // javascript
console.log(string.toUpperCase())   // JAVASCRIPT

// 1-7. 문자열 합치기 - concat(합칠문자열)
console.log(string.concat("!"))     // Javascript!
console.log(string.concat("!"," ","test"))    // Javascript! test
console.log(string.concat(["!",1,"test"]))    // Javascript!,1,test

// 1-8. 문자열 양끝 공백 제거 - trim()
string2 = "     javascript      "
console.log(string2.trim())     //javascript


/******** 2. 배열과 객체 연습 ********/
// 2-1. 원소 추가
var object = {}
object.string = "value"
object.array = [1,2,3]
object.object = {}
console.log(object)     // { string: 'value', array: [ 1, 2, 3 ], object: {} }

// 2-2. 객체 복사
// call by reference로 인해 object가 가리키는 값과 object2가 가리키는 값이 같다.
var object = {}
var object2 = object
object2.change = true
console.log(object2)     // { change: true }
console.log(object)     // { change: true }

var object3 = JSON.parse(JSON.stringify(object))
object3.change = false
console.log(object)     // { change: true }
console.log(object)     // { change: true }

// 2-3. 배열의 for문 활용하기
var array = ["K", "N", "Y"]
// (1) in을 사용하면 배열의 인덱스가 반환된다.
for(var index in array){
    console.log(index) // 0, 1, 2
}
// 0
// 1
// 2

// (2) of를 사용하면 배열의 원소가 반환된다.
for(var item of array){
    console.log(item)
}
// K
// N
// Y

// (2) entries()를 활용하여 [index, item]로 구성된 배열을 생성하여 사용한다. >> 이떄는 of를 사용해야함
for(var [index, item] of array.entries()){
    console.log(index, item)
}
// 0 'K'
// 1 'N'
// 2 'Y'


// 2-4. 객체의 for문 활용하기
// [주의] object는 for of를 사용할 수 없다. >> TypeError: object is not iterable
var object = {key1 : 'value1', key2 : { deep: 'value2'}, key3 : ['value3']}
for(var key in object){
    console.log(key, object[key])
}
// key1 value1
// key2 { deep: 'value2' }
// key3 [ 'value3' ]

// 2-5. 객체 키 및 원소 배열 만들기 - Object.keys(), Object.values()
console.log(Object.keys(object))    // [ 'key1', 'key2', 'key3' ]
console.log(Object.values(object))      // [ 'value1', { deep: 'value2' }, [ 'value3' ] ]
// [추가] array는 iterable이므로 for of 문의 사용이 가능해진다.
for(var key of Object.values(object)){
    console.log(key)
}
// value1
// { deep: 'value2' }
// [ 'value3' ]

/******** 3. 배열의 메서드 ********/
// 3-1. 인자로 주어진 값을 합쳐서 새 배열을 만든다. - concat()
var array = [1,2]
console.log(array.concat(3,4,5))        // [ 1, 2, 3, 4, 5 ]
console.log(array.concat([3,4,5]))      // [ 1, 2, 3, 4, 5 ]
console.log(array.concat(3,[4,5]))      // [ 1, 2, 3, 4, 5 ]
console.log(array)      // [ 1, 2 ] - 원본 안 바뀜

// 3-2. 배열의 원소를 돌면서 조건 테스트하기
// (1) every() : 배열의 모든 원소가 해당 조건을 통과하는지 확인
console.log(array.every(el => el%2 == 0))   // false

// (2) some() : 배열의 원소 중 하나라도 조건을 만족하는지 확인
console.log(array.some(el => el%2 == 0))    // true

// 3-3. 배열을 전체를 특정 값으로 채운다. - fill()
// [주의] fill()은 원본이 바뀐다.
console.log(array.fill(5))  // [ 5, 5 ]
console.log(array)      // [ 5, 5 ]
 
// 3-4. 배열의 원소 중 해당 조건을 만족하는 원소만 반환한다. - filter()
array = [1,2,3,4,5]
console.log(array.filter(el => el < 3)) // [ 1, 2 ]
console.log(array)  // [ 1, 2, 3, 4, 5 ]

// 3-5. 배열 원소마다 어떤 작업을 수행 - forEach() 
array.forEach(el => console.log(el*2))
// 2
// 4
// 6
// 8
// 10
// [주의] forEach 문은 반환 값이 없고 원본을 변경하지 않는다.
console.log(array.forEach(el => console.log(el*2))) // undefined

// 3-6 : 배열에 해당 값이 들어있는지 검사 - includes()
console.log(array.includes(2))  // true

// 3-7. 배열에 어떤 값이 있다면 index를 반환하고 없다면 -1 반환 - indexOf(), lastIndexOf()
array = [1,2,3,2,1]
console.log(array.indexOf(2))   // 1
console.log(array.lastIndexOf(2))   // 3

// 3-8 : 모든 문자를 연결해 하나의 문자로 만든다. - join(연결자)
array = [1,2,3]
console.log(array.join())       // 1,2,3 - 기본 구분자는 ','
console.log(array.join("-"))    // 1-2-3
console.log(array.join(""))     // 123

// 3-9 : 배열 내의 모든 값에 어떤 조건을 수행(forEach와 비슷)하고 결과를 모아서 배열로 리턴 - map()
array = [1,2,3,4,5]
console.log(array.map(el => el*2))  // [ 2, 4, 6, 8, 10 ]
console.log("변화있음?",array)
// 3-10 : 배열의 원소 추가 삭제 - 당연히 원본에 변화 있음
// (1) push() : 배열의 맨 뒤에 원소 추가
array.push(6)
console.log(array)  // [ 1, 2, 3, 4, 5, 6 ]

// (2) pop() : 배열의 맨 뒤의 원소 삭제
array.pop()
console.log(array)  // [ 1, 2, 3, 4, 5]

// (3) unshift() : 배열의 맨 앞에 원소 추가
array.unshift(0)
console.log(array)  // [ 0, 1, 2, 3, 4, 5]

// (4) shift() : 배열의 맨 앞의 원소 삭제
array.shift(0)
console.log(array)  // [ 1, 2, 3, 4, 5]

// 3-11 : 배열의 원소마다 누적 계산값과 함께 함수를 적용하여 하나의 값을 리턴 - reduce(), reduceRight() 
array = [1,2,3]
console.log(array.reduce((a, b)=> a-b))         // -4 : (1-2)-3 = -4
console.log(array.reduceRight((a, b)=> a-b))    // 0 : (3-2)-1 = 0

// 3-12 : 배열의 원소를 뒤집음 - reverse()
// [주의] 원본이 바뀜
console.log(array.reverse())    // [ 3, 2, 1 ]
console.log(array)      // [ 3, 2, 1 ]

// 3-13 : 배열의 start부터 end-1까지 shallow copy하는 메소드 slice(start, end)
// - end는 생략 가능
// [주의] 얕은 복사라는 점을 주의하자.
array = [1,2,3,4,5]
console.log(array.slice(1))     // [ 2, 3, 4, 5 ]
console.log(array.slice(0,3))   // [ 1, 2, 3 ]

// 3-14 : splice(start, 삭제할 원소 개수, item1, item2, ...)
// - 배열의 원소를 start부터 삭제하거나 새로운 원소(item1, item2, ...)를 추가한다.
// - 원본이 바뀐다.
// [주의] 삭제된 장소에 값이 삽입된다.
console.log(array.splice(3))    // [ 4, 5 ] - 인덱스 2번 원소부터 끝까지 삭제될 배열 리턴
console.log(array)      // [ 1, 2, 3 ]

console.log(array.splice(2,1))  // [3] - 삭제될 원소
console.log(array)      // [ 1, 2 ]


console.log(array.splice(1,1,6,7,8))  // [2] - 삭제될 원소
console.log(array)      // [ 1, 6, 7, 8 ]

console.log(array.splice(1,1,[6,7,8]))  // [6] - 삭제될 원소
console.log(array)      // [ 1, [ 6, 7, 8 ], 7, 8 ]

// 3-15 : sort() : 유니코드 순으로 배열을 정렬한다.
// - 원본이 바뀐다.
array = [1,3,4,5,2]
console.log(array.sort())   // [ 1, 2, 3, 4, 5 ]
console.log(array.sort((a,b)=>a-b)) // [ 1, 2, 3, 4, 5 ] : a,b 순으로 들어오는 값을 a-b > 0 일때 바꾸라는 말은 a > b 이면 안된다는 말 >> 즉, a < b 순으로 정렬 : 오름차순
console.log(array.sort((a,b)=>b-a)) // [ 5, 4, 3, 2, 1 ] : b-a 이므로 내림차순
console.log(array)  // [ 5, 4, 3, 2, 1 ] 

// 3-16 : 배열의 원소를 문자열로 변경 - toString() 
console.log(array.toString())   // 5,4,3,2,1

// 3-17 : Array.from(사용될 유사배열, callback) 
// - 유사 배열을 얕게 복사해 배열로 변환해주는 역할
// - 문자열을 배열로 변환
console.log(Array.from("javascript"))   // [ 'j', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't' ]
console.log(Array.from(array, el => el*2))  // [ 10, 8, 6, 4, 2 ]


/******** 4. 정렬 ********/
// 4-1. 숫자 정렬
var arrNumber = [1,2,4,5,3,2];
// (1) 오름차순 정렬
arrNumber.sort()
console.log(arrNumber)  // [ 1, 2, 2, 3, 4, 5 ]

arrNumber.sort((a,b) => a-b)
console.log(arrNumber)  // [ 1, 2, 2, 3, 4, 5 ]

// (2) 내림차순 정렬
arrNumber.sort((a,b) => b-a)
console.log(arrNumber)  // [ 5, 4, 3, 2, 2, 1 ]

// 4-2. 문자열 정렬
var arrString = ["가","다","마","나","라","바"]
// (1) 오름차순 정렬
arrString.sort()
console.log(arrString)  // [ '가', '나', '다', '라', '마', '바' ]

arrString.sort((a,b) => a > b)
console.log(arrString)  // [ '가', '나', '다', '라', '마', '바' ]

// (2) 내림차순
arrString.sort().reverse()
console.log(arrString)  // [ '바', '마', '라', '다', '나', '가' ]

arrString.sort((a,b) => b > a)
console.log(arrString)  // [ '바', '마', '라', '다', '나', '가' ]

// 4-3. 2차원 배열의 정렬
var array2 = [[2, "SFO"], [10, "ATL"], [5, "ATL"], [5, "ICN"], [7, "SFO"]]
// (1) 숫자를 기준으로 오름차순 정렬
array2.sort((arr1, arr2) => arr1[0] - arr2[0])
console.log(array2)
// [ [ 2, 'SFO' ],
//   [ 5, 'ATL' ],
//   [ 5, 'ICN' ],
//   [ 7, 'SFO' ],
//   [ 10, 'ATL' ] ]

// (2) 문자를 기준으로 오름차순 정렬
// [주의] 문자열끼리 빼면 난수가 나오므로 부등호를 사용하자
array2.sort((arr1, arr2) => arr1[1] > arr2[1])
console.log(array2)
// [ [ 5, 'ATL' ],
//   [ 10, 'ATL' ],
//   [ 5, 'ICN' ],
//   [ 2, 'SFO' ],
//   [ 7, 'SFO' ] ]

// (3) 숫자를 기준으로 오름차순 정렬한 뒤, 숫자가 같으면 문자열로 오름차순 정렬
var array2 = [[2, "SFO"], [10, "ATL"], [5, "ICN"], [5, "SFO"], [5, "ATL"], [7, "SFO"]]
array2.sort((arr1, arr2) => {
    // 숫자 기준 오름차순 정렬
    if(arr1[0] == arr2[0]){
        return arr1[1] > arr2[1]
    }
    return arr1[0] > arr2[0]
    
})
console.log(array2)

// [ [ 2, 'SFO' ],
//   [ 5, 'ATL' ],x
//   [ 5, 'ICN' ],
//   [ 5, 'SFO' ],
//   [ 7, 'SFO' ],
//   [ 10, 'ATL' ] ]


/******** 5. 문제풀이 ********/
// [문제 1] i번째 인덱스의 값이 i+1인 길이 10의 배열을 만드시오.
var array = Array(10).fill(null).map((item, index) => index+1)
console.log(array)  // [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

// [문제 2] (독립된) 2차원 배열을 만드시오.
// (잘못된 예)
var array = Array(2).fill([]) // 이때 []는 같은 주조를 넣는 것과 같다.
array[0][0] = 1
console.log(array)  // [ [ 1 ], [ 1 ] ]

// (올바른 예)
var array = Array(2).fill(null).map(el => [])
array[0][0] = 1
console.log(array)  // [ [ 1 ], [] ]

// [문제 3] [1,2,4,5] 배열의 중간에 3을 삽입하시오.
var array = [1,2,4,5]
array.splice(2,0,3)
console.log(array)  // [ 1, 2, 3, 4, 5 ]

// [문제 4] [[1],[2],[3],[4]] 를 deepcopy 하시오.
var array = [[1],[2],[3],[4]]
var copy_arr = JSON.parse(JSON.stringify(array))

// [문제 5] 2차원 배열의 중복을 제거하라.
function get_unique_array(arr,arrUnique){
    if(arr.length != 0){
        arrUnique.push(arr.filter((item, index) => {
            return arr.slice(index+1).every(el => {
                // 두배열이 같은 값인지는 JSON으로 변환해서 검사하는게 빠름
                return JSON.stringify(item) !== JSON.stringify(el)
            })
        }))
    }
    return arrUnique
}
console.log(get_unique_array([[1],[1,2],[],[],[1],[2],[1]], []))


// [문제 6] 다차원 배열의 빈 배열 제거
var array = [[1],[1,2],[],[],[1],[2],[1]]
console.log(array.filter(item=>item.length > 0))

// [문제 7] 1차원 배열의 중복 제거
arr = [1,2,2,2,2,3,4,5,3,4]
console.log(arr.filter((item, index)=>{
    return arr.indexOf(item) == index
}))

// [문제 8] : "HELLO HELLO HI HELLO" 에서 모든 HELLO를 HI로 바꿔라
var sting = "HELLO HELLO HI HELLO"
console.log(sting.split("HELLO").join("HI"))

// [문제 9] : [1,2,4,8,16,32] 배열을 만들어라
// [문제 10] : [1,2,3,5,6] splice()를 사용하여 [1,2,3,4,5,6]을 만들어라

