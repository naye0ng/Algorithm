/* 자바스크립트 문자열 메소드 */

// [1] : chatAt(index) : 지정된 위치의 문자열 데이터 반환
var strTatget = "HELLO";
console.log(strTatget.charAt(1))    // E

 
// [2] : indexOf(), lastIndexOf() 
console.log(strTatget.indexOf("L"))    // 2
console.log(strTatget.lastIndexOf("L"))    // 3


// [3] : replace("찾을 문자", "치환할 문자") 
strTatget = "HELLO WORD!";
console.log(strTatget.replace("HELLO", "HI"))   // HI WORD!
console.log(strTatget)  // HELLO WORD! - 당연히 원본 안바뀜
// 그러나 왼쪽에서 처음 나오는 문자열만 치환됨


// [4] : substring(시작인덱스, 끝날인덱스) : 시작점 ~ 끝점-1
// [4] : substr(시작인덱스, 문자개수) : 시작점부터 문자개수 반환
strTatget = "HELLO WORD!";
console.log(strTatget.substring(0,5))   // HELLO
console.log(strTatget.substr(1,3))     // ELL
console.log(strTatget)  // HELLO WORD! - 당연히 원본 안바뀜


// [5] : split("문자") : 문자를 기준으로 잘라 배열로 반환
strTatget = "HELLO WORD!";
console.log(strTatget.split(" "))   // [ 'HELLO', 'WORD!' ]


// [6] : toLowerCase(), toUpperCase()
strTatget = "HELLO WORD!";
console.log(strTatget.toLowerCase())   // hello word!


// [7] : concat("합칠 문자열")
strTatget = "HELLO";
console.log(strTatget.concat(" ","WORD"))   // HELLO WORD
console.log(strTatget)  // HELLO


// [8] : trim() : 문자열 양끝 공백 제거
strTatget = " HELLO ";
console.log(strTatget.trim())   // HELLO
console.log(strTatget)  // " HELLO " - 원본 변화 없음


// [문제 1] : "HELLO HELLO HI HELLO" 에서 모든 HELLO를 HI로 바꿔라
strTatget = "HELLO HELLO HI HELLO"
console.log(strTatget.split("HELLO").join("HI"))