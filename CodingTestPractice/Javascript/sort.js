/* [1] 숫자 정렬 */
const A = [1,2,4,5,3,2];
const B = [1,2,4,5,3,2];

// 오름차순 
A.sort((a,b)=>{
    // 양수 : 자리 바꿈, 음수 : 이미 정렬된 상태
    // a-b의 값이 양수이면 a > b이므로 자리바꿔야 한다. 오름차순은 작 => 큰
    return a - b; 
})
console.log(A)  // [ 1, 2, 2, 3, 4, 5 ]

// 내림차순 
B.sort((a,b)=>{
    return b - a;
})
console.log(B);  // [ 5, 4, 3, 2, 2, 1 ]


/* [2] 문자열 정렬 */
const C = ["가","다","마","나","라","바"];
const D = ["가","다","마","나","라","바"];
const E = ["가","다","마","나","라","바"];

// 오름차순(작 => 큰)
C.sort();
console.log(C);

// 내림차순(1)
D.sort().reverse();
console.log(D);

// 내림차순(2)
E.sort((a,b)=>{
    // 내림차순은 큰=>작 순서대로 즉, 작(a), 큰(b) 순서일때 뒤집어야함
    // 문자열의 경우 - 연산의 결과값은 Nan 이므로 부등호를 사용하자
    return b > a;
})
console.log(E)


/* 2차원 배열의 정렬 */
const F = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]];
const G = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]];
const H = [["ICN", "SFO"], ["ICN", "ATL"], ["ICN", "BTL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]];

// arr[0] 값을 기준으로 오름차순 정렬
// 오름차순은 작 => 큰 즉, 앞(a)이 뒤(b)보다 큰 경우 변경
F.sort((a,b) => {
    return a[0] > b[0];
})
console.log(F);

// arr[1] 값을 기준으로 오름차순 정렬
G.sort((a,b) => {
    return a[1] > b[1];
})
console.log(G);

// arr[0]에 대해선 오름차순(작 => 큰), arr[1]에 대해 내림차순
var array2 = [[2, "SFO"], [10, "ATL"], [5, "ICN"], [5, "SFO"], [5, "ATL"], [7, "SFO"]]
array2.sort((arr1, arr2) => {
    // 숫자 기준 오름차순 정렬
    if(arr1[0] == arr2[0]){
        return arr1[1] > arr2[1]
    }
    return arr1[0] > arr2[0]
    
})
console.log(array2)
// (아래 코드는 틀림)
// H.sort((a,b) =>{
//     // 0 : 앞이 클때 변경
//     // 1 : 뒤가 클때 변경
//     return a[1] < b[1] || a[0] > b[0];
// })
// console.log(H);

function ascending(a, b){
    if(a > b) return true
    return false
}

function descending(a, b){
    if(a < b) return true
    return false
}

var array = [[2, "SFO"], [10, "ATL"], [5, "ICN"], [5, "SFO"], [5, "ATL"], [7, "SFO"]]
// [1] 0번 인자에 대한 오름차순 정렬
array.sort((arr1, arr2) => ascending(arr1[0], arr2[0]))
console.log(array)

// [2] 0번 인자에 대한 내림차순 정렬
array.sort((arr1, arr2) => descending(arr1[0], arr2[0]))
console.log(array)

// [3] 1번 인자에 대한 오름차순 정렬
array.sort((arr1, arr2) => ascending(arr1[1], arr2[1]))
console.log(array)

// [4] 1번 인자에 대한 내림차순 정렬
array.sort((arr1, arr2) => descending(arr1[1], arr2[1]))
console.log(array)

// [4] 0번 인자에 대한 오름차순 정렬 + 1번 인자에 대한 내림차순 정렬
var array = [[2, "SFO"], [5, "ATL"], [10, "ATL"], [5, "ICN"], [5, "SFO"], [7, "SFO"]] // 정렬안됨
array.sort((arr1, arr2) => {
    // 같을 때 저리 필요함...
    // var array = [[2, "SFO"], [5, "ATL"], [10, "ATL"], [5, "ICN"], [5, "SFO"], [7, "SFO"]]
    return ascending(arr1[0], arr2[0]) ? true : descending(arr1[1], arr2[1])
})


// [주의] 자바스크립트의 sort는 내부적으로 >, < 비교를 수행하며 string 비교를 진행한다. 즉, 2 > 10으로 정렬된다.
// 숫자 정렬을 하고 싶다면 -연산을 사용하는 습관을 들이자... 아니면 따로 콜백함수를 제작(ascendig)해주자!!
array = [1,2,10]
console.log(array.sort())   //[ 1, 10, 2 ]
array.sort((a,b) => ascending(a,b))
console.log(array)  // [ 1, 2, 10 ]