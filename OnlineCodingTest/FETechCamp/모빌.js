function solution(weights) {
    if(weights.length == 1){return 1}
    var array = weights.map(el=>[el,1]).sort((w1, w2)=> w1[0]-w2[0])

    // 맨 아래 모빌은 항상 두 개씩 짝지어짐
    var is_not_stop = true
    var next_array = []
    while(is_not_stop){
        is_not_stop = false
        next_array = []

        for(var i=0;i<array.length-1;i++){
            if(array[i][1] > 0){
                // 다음값과 같은 값이라면 묶기
                if(array[i][0] == array[i+1][0]){
                    is_not_stop = true
                    next_array.push([array[i][0]*2, array[i][1]+array[i+1][1]])
                    array[i][1] = 0
                    array[i+1][1] = 0
                }
                else{
                    next_array.push([array[i][0], array[i][1]])
                }
            }
        }
        // 마지막값 확인
        if(array[array.length-1][1] > 0){
            next_array.push([array[array.length-1][0], array[array.length-1][1]])
        }

        array = next_array.sort((w1, w2)=> w1[0]-w2[0])
    }

    return array.sort((w1, w2)=> w2[1]-w1[1])[0][1]
}

// [16,16,16,16,16,16,16,16,1,1,2,4,4]
// 8
