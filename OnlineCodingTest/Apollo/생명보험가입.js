function getInsuranceComb(table, benefits, depth, i) {
    if(benefits.indexOf(false) == -1) {
        answer = Math.min(answer, depth)
    }else if(depth < answer){
        for(let k = i; k < table.length; k++){
            const newBenefits = JSON.parse(JSON.stringify(benefits))
            table[k].forEach((value, index)=>{
                if(value === 'O'){
                    newBenefits[index] = true
                }
            })
            getInsuranceComb(table, newBenefits, depth+1, k+1)
        }
    }
}

let answer = 0
function solution(table) {
    answer = table.length
    table = table.map(v => v.split(''))
    const benefits = Array(table[0].length).fill(false)
    getInsuranceComb(table, benefits, 0, 0)
    return answer
}

console.log(solution(["OXOXO", "OOOOO", "XOXOX"]))
