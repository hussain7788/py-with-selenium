// one child class gets the props form one parent class is called single inheritance 

class Person{
    name:string;
    age:string
    constructor(name, age){
        this.name = name
        this.age = age

    }
}
class Student_class extends Person{
    rollno:number;
    marks:number;
    constructor(name, age, rollno, marks){
        super(name, age)
        this.rollno = rollno
        this.marks = marks
    }
}

let s = new Student_class("hussain", 23, 12345, 100)
console.log(s.name, s.age, s.rollno, s.marks)