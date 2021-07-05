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
var Employee = /** @class */ (function () {
    function Employee(empName, empAge) {
        this.companyName = "tcs";
        this.companyAddress = "hyd";
        var empname = empName;
        var empage = empAge;
        console.log(empage, empname);
    }
    Employee.prototype.greet = function () {
        console.log("my company name is " + this.companyName + " and my address is " + this.companyAddress);
    };
    return Employee;
}());
// let d1 = new Employee("hussain", 23);
// console.log(d1.companyAddress);
// console.log(d1.companyName);
// d1.greet()
var Manager = /** @class */ (function (_super) {
    __extends(Manager, _super);
    function Manager(managerName, managerAge) {
        return _super.call(this, managerName, managerAge) || this;
    }
    Manager.prototype.delegate = function () {
        console.log("worked");
    };
    return Manager;
}(Employee));
var m1 = new Manager("kanna", 23);
m1.greet();
m1.delegate();
