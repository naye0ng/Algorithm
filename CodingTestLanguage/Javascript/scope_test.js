function test(){
    var a = 10;
    console.log("1",a) //10
    function test2(i){
        if(i < 3){
            a += 10;
            console.log(i, a) //20
            test2(i+1)
        }
    }
    test2(0);
    console.log("3",a) //20
}


a = [1,3,4,56,6]
console.log(a)
b = a
b[1] = 10;
console.log(a)


console.log([1]==[1])