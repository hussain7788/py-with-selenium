class Employee{
    companyName:string = "tcs";
    companyAddress :string = "hyd";

    constructor(empName:String, empAge:Number){
        let empname = empName
        let empage = empAge
        console.log(empage,empname);

    }
        
    greet(){
        console.log(`my company name is ${this.companyName} and my address is ${this.companyAddress}`)
    }
}

// let d1 = new Employee("hussain", 23);
// console.log(d1.companyAddress);
// console.log(d1.companyName);
// d1.greet()

class Manager extends Employee{
    constructor(managerName:string, managerAge:number){
        super(managerName, managerAge);
    }
    delegate(){
        console.log("worked")
    }
}
let m1 = new Manager("kanna", 23)
m1.greet();




