// interface person {
//     name: string;
//     age: number;
//     add: string;
//     number: number;
// }
// interface employee {
//     emp_degn: string;
//     emp_salary: number;
//     emp_id: number;
// }

// class teacher{
//     teacherName:string;
//     teacheradd
//         constructor(p: person, e:employee){
//             console.log(`my name is ${p.name} and my age is ${p.age} and address is ${p.add} and number is ${p.number}`)
//             console.log(`emp degn is ${e.emp_degn} and salary is ${e.emp_salary} and id is ${e.emp_id}`)
//         }

// }
// var d1 = {"name":"hussain", "age":23, "add":"kadapa", "number":8179464351}
// var d2 = {"emp_degn":"developer", "emp_salary":50000, "emp_id":1}

// var t1 = new teacher(d1, d2);
// t1.teacherName;



interface one{
    name:string;
    age:number;
}

interface two{
    person:one;
    e_degn:string;
    e_salary:number;
}

abstract class sample {
    sample_method(p:one, e:two){
        console.log(`name ${p.name} and age ${p.age}`)
        console.log(`person ${e.person.name} and degn ${e.e_degn} salary ${e.e_salary}`)

    }
}
class new_sample extends sample{
    new_sample_var:string = "sample"

}
let dict1 = {"name":"valli", "age":23}
let dict2 = {"person":dict1, "e_degn":"developer", "e_salary":40000}
let ns = new new_sample();
ns.sample_method(dict1, dict2)