// interfaces we can pass to other function
function Concate(person) {
    console.log("Name is:", person.firstName + person.lastName);
}
var p = { firstName: "valli", lastName: "hussain" };
Concate(p);
