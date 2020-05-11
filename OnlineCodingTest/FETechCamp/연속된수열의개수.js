function get_frequency_array(arr){
    var frequency = Array(1001).fill(0)
    var index = 0
    var before = arr[0]
    frequency[index]++
    for(var i=1;i<arr.length;i++){
        if(before != arr[i]){
            before = arr[i]
            index++
        }
        frequency[index] ++
    }
    return frequency.filter(el=>el>0)
}

function solution(arr) {
    var answer = 0
    while(arr.length != 1 || arr[0] != 1){
        answer++
        arr = get_frequency_array(arr)
    }
    return answer;
}

// 입력 : [1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3]
// 답 : 6


// var a = [16, 16, 16, 16, 16, 16, 16, 16, 1, 1, 2, 4, 4]
// // 차이나는 이유?
// var a2 = a.map(el=>[el,1]).sort((a,b)=>a[0]-b[0])
// var a2 = a.map(el=>[el,1]).sort((a,b)=>a[0]>b[0])
// console.log(a2)
