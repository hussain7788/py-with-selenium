// interfaces we can pass to other function

interface Person{
    firstName:string;
    lastName:string;
}

function Concate(person:Person){
    console.log("Name is:", person.firstName + person.lastName)
}

let p = {firstName:"valli", lastName:"hussain"}
Concate(p)
