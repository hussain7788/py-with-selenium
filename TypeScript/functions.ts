function Sum(a:number, b?:number){
    // the quesion mark is oprional param
    if(b){
        console.log(a*b)
    }
    else{
        console.log(a)
    }
}
Sum(10);


interface fun1{
    a:number;
    b?:number;

}
function sample_func(data:fun1){
        if(data.a < data.b){
            console.log("addition is:", data.a+data.b)
        }
        else if(data.a > data.b){
            console.log("substractions is:", data.a-data.b)

        }
        else if(data.a == data.b){
            console.log("multiplications is:", data.a*data.b)

        }
        else {
            console.log("not valid")
        }
}
let dic1 = {"a":4, "b":2}
sample_func(dic1)


//// arrow functions 
let sum = (f:fun1) => {
    if (f.a && f.b){
        console.log("division is:", f.a%f.b)
    }
}
sum(dic1)
function loop(a:any[]){
    for(let i=0; a.length>i; i++){
        console.log(a[i])

    }

}
loop([1,2,3])

// these 3 dots defindes rest parameter ..means we can number of variables as we want and returns in list ..
function dot_param(a:number, ...b:number[]){
    let data:any = [];
    for(let i=0; b.length>i; i++){
        data.push(b[i])
        // console.log(b[i])
    }
    data.push(40,50)
    console.log("data is:", data)
    //pop will remove last ele in array
    data.pop()
    console.log("data is:", data)


}
dot_param(10, 20,30)