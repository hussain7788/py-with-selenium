var Engine = /** @class */ (function () {
    function Engine() {
    }
    Engine.prototype.get_engine = function () {
        // console.log("get engine")
        return 4 - 2;
    };
    Engine.prototype.get_mtd = function () {
        this.get_engine();
    };
    return Engine;
}());
var Tyres = /** @class */ (function () {
    function Tyres() {
    }
    Tyres.prototype.get_tyres = function () {
        return 2 + 4;
    };
    return Tyres;
}());
var Car = /** @class */ (function () {
    function Car(e, t) {
        console.log("engine is", e.get_engine(), "tyres are", t.get_tyres());
    }
    return Car;
}());
function sample(e, t) {
    console.log("e is", e.get_mtd(), t.get_tyres());
}
var t = new Tyres();
var e = new Engine();
// let c1= new Car(e, t)
sample(e, t);
