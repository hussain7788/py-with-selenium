// class Employee {
//     companyName: string = "tcs";
//     companyAddress: string = "hyd";

//     constructor(empName: String, empAge: Number) {
//         let empname = empName
//         let empage = empAge
//         console.log(empage, empname);

//     }

//     greet() {
//         console.log(`my company name is ${this.companyName} and my address is ${this.companyAddress}`)
//     }
// }

// // let d1 = new Employee("hussain", 23);
// // console.log(d1.companyAddress);
// // console.log(d1.companyName);
// // d1.greet()

// class Manager extends Employee {
//     constructor(managerName: string, managerAge: number) {
//         super(managerName, managerAge);
//     }
//     delegate() {
//         console.log("worked")
//     }
// }
// let m1 = new Manager("kanna", 23)
// m1.greet();
// m1.delegate()


interface person_interface{
    name:string;
    age:number;
    add?:string;
}


class person{
    constructor(p:person_interface){
        let p_name = p.name;
        let p_age = p.age;
        let p_add = p.add;

        console.log(`name is ${p_name} age is ${p_age} address is ${p_add}`)
    }
   // arrow function be like this-------
    get = (b:person_interface) => {

        console.log(`name is ${b.name} age is ${b.age} address is ${b.add}`)
        console.log("get method")}

}

let p = new person({"name":"hussain", "age":23, "add":"kadapa"})
p.get({"name":"valli", "age":23,})


class extend_p extends person{
    constructor(p:person_interface){
        super(p);
    }
}

let ex_p = new extend_p({"name":"hussain", "age":23, "add":"kadapa"})
ex_p.get({"name":"hussain", "age":23, "add":"kadapa"})