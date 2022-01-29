// interfaces we can pass to other function
function Concate(person) {
    console.log("Name is:", person.firstName + person.lastName);
}
var p = { firstName: "valli", lastName: "hussain" };
Concate(p);
var triangle = /** @class */ (function () {
    function triangle() {
        this.name = "hussain";
    }
    triangle.prototype.draw = function () {
        console.log("this is triangle", this.name);
    };
    return triangle;
}());
var square = /** @class */ (function () {
    function square() {
        this.name = 'valli';
    }
    square.prototype.draw = function () {
        console.log("this is square", this.name);
    };
    return square;
}());
var newShape = /** @class */ (function () {
    function newShape(s) {
        s.draw();
    }
    return newShape;
}());
var s1 = new square();
var t = new triangle();
var n = new newShape(s1);
