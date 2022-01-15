// one child class gets the props form one parent class is called single inheritance 
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
var Person = /** @class */ (function () {
    function Person(name, age) {
        this.name = name;
        this.age = age;
    }
    return Person;
}());
var Student_class = /** @class */ (function (_super) {
    __extends(Student_class, _super);
    function Student_class(name, age, rollno, marks) {
        var _this = _super.call(this, name, age) || this;
        _this.rollno = rollno;
        _this.marks = marks;
        return _this;
    }
    return Student_class;
}(Person));
var s = new Student_class("hussain", 23, 12345, 100);
console.log(s.name, s.age, s.rollno, s.marks);
