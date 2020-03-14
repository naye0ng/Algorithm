// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	console.log("Hello Goorm! Your input is", line);

}).on("next", function(line) {
	console.log("Hello Goorm! Your input is", line);
	rl.close();
}).on("close", function() {
	process.exit();
});


/*
6 3 10 3 10
3 7
3 7
5 6
3 1
10 10
1 1
*/