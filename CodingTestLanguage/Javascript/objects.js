var obj = {}
// obj.a = [1,2]
obj.b = {c:1}

var obj2 = JSON.parse(JSON.stringify(obj))
obj.c = 3
console.log(obj2)

var foo = {
    deep: {
        key: 'value'
    },
    shallow: false
};
var bar = JSON.parse(JSON.stringify(foo));
foo.deep.key = 'other value';

console.log(foo);
console.log(bar);

var arr = [2,3,4]
for(var a in arr){
    console.log(a) // index
}

for(var a of arr){
    console.log(a) // value
}

for([index, item] of arr.entries()){
    console.log(index, item)
}

for(var key in obj){
    console.log(key) 
}

console.log(Object.keys(obj))