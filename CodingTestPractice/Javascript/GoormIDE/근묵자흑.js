const readline = require('readline');

(async () => {
    const getCount = (C) => {
        const q = parseInt(C/(K-1))
        if(C%(K-1) === 0) return q
        return q+1
    }

    const getChangeCount = () => {
        const min = Math.min(...numbers)
        const i = numbers.indexOf(min)

        let answer = N
        let [front, back] = [0,0]
        for(let k = 0; k < K; k++){
            front = i-k
            back = N-(i+1)-(K-(k+1))
            if(front >= 0 && back < N){
                answer = Math.min(answer, 1+getCount(front)+getCount(back))
            }
        }
        return answer
        
    }

    let rl = readline.createInterface({ input: process.stdin });
    let [N, K] = [0,0]
    let numbers = []
    for await (const line of rl) {
        if(N == 0){
            [N, K] = line.split(' ').map(v => v*1)
            continue
        }

        numbers = line.split(' ').map(v => v*1)
        console.log(getChangeCount())
        rl.close();
    }
    process.exit();
})();