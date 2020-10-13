// const readline = require('readline');

// const rl = readline.createInterface({
// 	input: process.stdin,
// 	output: process.stdout
// });

// rl.on('line', function(answer) {
// 	console.log(answer);
// 	rl.close();
// });

// round, ceil, floor ( 반올림, 올림, 내림 )

// 10 -> 2
var dec = 123; 
var bin = dec.toString(2);
console.log(bin)
// 2 -> 10
var dec = parseInt(bin, 2);
console.log(dec)

// 2진수 -> 16진수
// 2-> 10->16
var hex = parseInt(bin, 2).toString(16)

// 십진수숫자.toString(진수) - 10진수 숫자를 해당 진수로 바꿔서 리턴 : 10 => n진수
// parseInt(숫자, 현재 숫자의 진수) - 현재 숫자의 진수를 10진수로 변경 : n진수 => 10
let d = 123
console.log(d.toString(9))
 

// 아스키 코드 치환하기
let a = 'A'
let code = a.charCodeAt()
console.log(code)
console.log(String.fromCharCode(code))


console.log(typeof (10).toString(6))

d = '1234'
let f = 1
for(let n of d){
    f *= n*1
}

console.log(f)


console.log((10).toString(2))