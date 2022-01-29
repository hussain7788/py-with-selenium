class Engine{
    
    get_engine(){
        // console.log("get engine")
        return 4-2
    }
    get_mtd(){
        return this.get_engine()
    }
}
class Tyres{
   
    get_tyres(){
        return 2+4
    }
}

class Car{
    constructor(e:Engine, t:Tyres)
    {
        console.log("engine is", e.get_engine(), "tyres are", t.get_tyres())
        
    }
}

function sample(e:any, t:any){
    console.log("e is", e.get_mtd(), e.get_engine(), t.get_tyres());
    
}
let t = new Tyres()
let e= new Engine()

// let c1= new Car(e, t)
sample(e, t)