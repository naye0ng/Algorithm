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