const readline = require('readline');

(async () => {
    const checkQuestion = (questions) => {
        const difficulty = {}
        for (let q of questions) {
            if (difficulty[q] == null) {
                difficulty[q] = true
            }
        }

        if (Object.keys(difficulty).length >= 3) return 'YES'
        return 'NO'
    }

    let rl = readline.createInterface({ input: process.stdin });

    let input = []
    for await (const line of rl) {
        input.push(line.split(' '))
        if(input.length == 2){
            console.log(checkQuestion(input[1]))
            rl.close();
        }
    }
    process.exit();
})();