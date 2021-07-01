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