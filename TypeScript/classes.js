// class Employee {
//     companyName: string = "tcs";
//     companyAddress: string = "hyd";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var person = /** @class */ (function () {
    function person(p) {
        // get(b:person_interface) {
        //     console.log(`name is ${b.name} age is ${b.age} address is ${b.add}`)
        //     console.log("get method")
        // }
        this.get = function (b) {
            console.log("name is ".concat(b.name, " age is ").concat(b.age, " address is ").concat(b.add));
            console.log("get method");
        };
        var p_name = p.name;
        var p_age = p.age;
        var p_add = p.add;
        console.log("name is ".concat(p_name, " age is ").concat(p_age, " address is ").concat(p_add));
    }
    return person;
}());
var p = new person({ "name": "hussain", "age": 23, "add": "kadapa" });
p.get({ "name": "valli", "age": 23 });
var extend_p = /** @class */ (function (_super) {
    __extends(extend_p, _super);
    function extend_p(p) {
        return _super.call(this, p) || this;
    }
    return extend_p;
}(person));
var ex_p = new extend_p({ "name": "hussain", "age": 23, "add": "kadapa" });
ex_p.get({ "name": "hussain", "age": 23, "add": "kadapa" });
