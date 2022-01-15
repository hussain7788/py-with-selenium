// this relation is like child and grandchild ..one child class gets props from another child class and that class gets from parent class

class m_person{
    name:string;
    age:number;
    constructor(name, age){
        this.name = name
        this.age = age
    }
    get_m_person(){
        console.log("this is m_person method")
    }
}

class m_employee extends m_person{
    emp_id:number;
    emp_degn:number;
    constructor(name, age, emp_id, emp_degn){
        super(name, age)
        this.emp_id = emp_id
        this.emp_degn = emp_degn
    }
    get_m_employee(){
        console.log("this is m_emp method")
    }

}
class m_teacher extends m_employee{
        salary:number;
        address:string;
        constructor(name, age, emp_id, emp_degn, salary, address){
            super(name, age, emp_id, emp_degn)
            this.salary = salary
            this.address = address
        }
        get_m_teacher(){
            console.log("this is m_teacher method")
        }
}
let e = new m_teacher("valli", 23, 1, "python developer", 50000, "kadapa")
console.log(e.name, e.age, e.emp_id, e.emp_degn, e.salary, e.address)
e.get_m_employee()
e.get_m_person()
e.get_m_teacher()