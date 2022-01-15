// interface Person {
//     set_p_data(): void;
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
var second = /** @class */ (function () {
    function second() {
    }
    second.prototype.Display = function () {
        console.log("this is Display mehtod");
    };
    return second;
}());
var interface_first = /** @class */ (function () {
    function interface_first() {
    }
    interface_first.prototype.first_interface = function () {
        var name = "hussain";
        var age = 23;
        console.log("this is first_interface method", name, age);
    };
    return interface_first;
}());
var ab_second = /** @class */ (function (_super) {
    __extends(ab_second, _super);
    function ab_second() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.ab_gender = "male";
        _this.ab_salary = 50000;
        return _this;
    }
    ab_second.prototype.Show = function () {
        console.log("this is show method from second abstract class");
    };
    return ab_second;
}(second));
var i1 = new interface_first();
i1.first_interface();
var ab = new ab_second();
ab.Show();
ab.Display();
console.log(ab.ab_gender);
console.log(ab.ab_salary);
