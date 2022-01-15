// // we have these data types in typesctipt

// // let result:boolean = true;
// let Name:string = "valli";
// let age:number = 23;
// let nothing:null = null;
// let myName: undefined = undefined;
// let Sentence:string = `my name is ${Name}.. i am exp person in typescript`

// console.log(Sentence)

// // declare array in ts
// let list1:number[] = [1,2,3,4]
// let list2:any = [2,3,4]
// console.log(list2)

// let person:[string, number]= ["hussain",23];

// //enum 
// // enum Color  {"red", "blue", "green"}
// // let c = Color.green;
// // console.log(c)

// // multiple type
// let mulType : number | string;
// mulType = "hussain";
// mulType = 23;



export {}
let Name:string = "hussain";
let age:number = 23;
let bool:boolean = true;
let null_type:null = null;
let undefined_type:undefined = undefined;
let list_type:any = ["name", "age"]
let list_type_2:number[] = [1,2,3,4]
let sequence:string = `my name is ${Name};
age is ${age}; my data is ${list_type.name}`

// publice methods and private methods 
class sample{
    public method_1(){
        console.log("this is public method so we can access outside of class ")
    }
    private method_2(){
        console.log("this is private methods ..so we cant access outside of class ")
    }
}

let i;
i = "valli"
var j;
j = "hussain"
const g:string = "saleem"


console.log("sequenc::", sequence)

