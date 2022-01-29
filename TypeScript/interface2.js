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
var sample = /** @class */ (function () {
    function sample() {
    }
    sample.prototype.sample_method = function (p, e) {
        console.log("name ".concat(p.name, " and age ").concat(p.age));
        console.log("person ".concat(e.person.name, " and degn ").concat(e.e_degn, " salary ").concat(e.e_salary));
    };
    return sample;
}());
var new_sample = /** @class */ (function (_super) {
    __extends(new_sample, _super);
    function new_sample() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.new_sample_var = "sample";
        return _this;
    }
    return new_sample;
}(sample));
var dict1 = { "name": "valli", "age": 23 };
var dict2 = { "person": dict1, "e_degn": "developer", "e_salary": 40000 };
var ns = new new_sample();
ns.sample_method(dict1, dict2);
var data = {
    "employees": [
        { "id": 1, "name": "anil", "age": 30 },
        { "id": 2, "name": "sunil", "age": 25 },
        { "id": 3, "name": "ajay", "age": 23 },
        { "id": 4, "name": "vijay", "age": 24 },
        { "id": 5, "name": "john", "age": 26 }
    ]
};
var res = data.employees.filter(function (value, index) {
    console.log(value.id);
});
console.log("result", res);
