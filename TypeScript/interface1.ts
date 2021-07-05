interface Person {
    set_p_data(): void;

}

interface Emp {

    set_emp_data(): void;
}

class Teacher implements Person, Emp {
    set_p_data(): void {
        console.log("set p data")
    }
    set_emp_data(): void {
        console.log("set emp data")
    }
}
let c1 = new Teacher;
c1.set_p_data();
c1.set_emp_data()