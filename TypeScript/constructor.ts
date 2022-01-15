class A
{
   constructor()
   {
     console.log("i am A class DC");
   }
}
class B extends A
{
    
   constructor(){
       super()
       console.log("this is class B")
   }
   
}
class C extends  B
{
    name:string;
    age:number;
   constructor(name:string, age:number)
   {
       super()
       this.name = name
       this.age = age
       console.log(`name : ${this.name} age : ${this.age}`)
       

   }
  
}
var c1:C=new C("hussain", 23);