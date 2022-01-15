// interface Person {
//     set_p_data(): void;

// }

// interface Emp {

//     set_emp_data(): void;
// }

// class Teacher implements Person, Emp {
//     set_p_data(): void {
//         console.log("set p data")
//     }
//     set_emp_data(): void {
//         console.log("set emp data")
//     }
// }
// let c1 = new Teacher;
// c1.set_p_data();
// c1.set_emp_data()



// interface with abstract methods 
interface first{
     first_interface():void;

}
abstract class second{
    ab_gender:string;
    ab_salary:number;
    abstract Show():void;
    Display():void{
        console.log("this is Display mehtod")

    }

}

class interface_first implements first{
    first_interface(): void {
        let name:string = "hussain";
        let age:number = 23
        console.log("this is first_interface method", name, age)
    }

}

class ab_second extends second{
    ab_gender = "male"
    ab_salary = 50000;
    Show(): void {
        console.log("this is show method from second abstract class")
    }

}

let i1 = new interface_first();
i1.first_interface();

let ab = new ab_second();
ab.Show();
ab.Display();
console.log(ab.ab_gender);
console.log(ab.ab_salary)
