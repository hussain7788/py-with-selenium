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



// #######################################################################
interface shape{
    name:string;
    draw();
}
class triangle implements shape{
    name: string ="hussain"
    draw() {
        console.log("this is triangle", this.name)
    }

}
class square implements shape{
    name: string = 'valli'
    draw() {
        
        console.log("this is square", this.name);
        
    }
}

class newShape{
    constructor(s:shape){
        s.draw()
        
    }
}
let s1 = new square()
let t= new triangle()
let n = new newShape(s1)
