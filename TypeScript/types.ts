// we have these data types in typesctipt

export {}
let result:boolean = true;
let Name:string = "valli";
let age:number = 23;
let nothing:null = null;
let myName: undefined = undefined;
let Sentence:string = `my name is ${Name}.. i am exp person in typescript`

console.log(Sentence)

// declare array in ts
let list1:number[] = [1,2,3,4]
let list2:any = [2,3,4]
console.log(list2)

let person:[string, number]= ["hussain",23];

//enum 
enum Color  {"red", "blue", "green"}
let c = Color.green;
console.log(c)

// multiple type
let mulType : number | string;
mulType = "hussain";
mulType = 23;