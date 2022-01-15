// this relation is like child and grandchild ..one child class gets props from another child class and that class gets from parent class
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
var m_person = /** @class */ (function () {
    function m_person(name, age) {
        this.name = name;
        this.age = age;
    }
    m_person.prototype.get_m_person = function () {
        console.log("this is m_person method");
    };
    return m_person;
}());
var m_employee = /** @class */ (function (_super) {
    __extends(m_employee, _super);
    function m_employee(name, age, emp_id, emp_degn) {
        var _this = _super.call(this, name, age) || this;
        _this.emp_id = emp_id;
        _this.emp_degn = emp_degn;
        return _this;
    }
    m_employee.prototype.get_m_employee = function () {
        console.log("this is m_emp method");
    };
    return m_employee;
}(m_person));
var m_teacher = /** @class */ (function (_super) {
    __extends(m_teacher, _super);
    function m_teacher(name, age, emp_id, emp_degn, salary, address) {
        var _this = _super.call(this, name, age, emp_id, emp_degn) || this;
        _this.salary = salary;
        _this.address = address;
        return _this;
    }
    m_teacher.prototype.get_m_teacher = function () {
        console.log("this is m_teacher method");
    };
    return m_teacher;
}(m_employee));
var e = new m_teacher("valli", 23, 1, "python developer", 50000, "kadapa");
console.log(e.name, e.age, e.emp_id, e.emp_degn, e.salary, e.address);
e.get_m_employee();
e.get_m_person();
e.get_m_teacher();
