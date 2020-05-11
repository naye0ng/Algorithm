function solution(reqs) {
    var accounts = []
    var limit = []
    var money = []

    var answer = [];
    for(var i=0;i<reqs.length;i++){
        var req = reqs[i].split(" ")

        if(req[0] == "CREATE"){
            if(accounts.indexOf(req[1]) >= 0){
                answer.push(403)
            }else{
                // 계좌 개설
                accounts.push(req[1])
                limit.push(-parseInt(req[2]))
                money.push(0)
                answer.push(200)
            }
        }else if(req[0] == "DEPOSIT"){
            var account = accounts.indexOf(req[1])
            if(account >= 0){
                // 입금
                money[account] += parseInt(req[2])
                answer.push(200)
            }else{
                answer.push(404)
            }
        }else{
            var account = accounts.indexOf(req[1])
            if(account >= 0){
                if(limit[account] > money[account]-parseInt(req[2])){
                    // 한도초과
                    answer.push(403)
                }else{
                    money[account] -= parseInt(req[2])
                    answer.push(200)
                }
            }else{
                answer.push(404)
            }
        }
    }
    return answer;
}

// 입력 : ["DEPOSIT 3a 10000", "CREATE 3a 300000", "WITHDRAW 3a 150000", "WITHDRAW 3a 150001"]
// 답 : [404, 200, 200, 403]