var Teacher = /** @class */ (function () {
    function Teacher() {
    }
    Teacher.prototype.set_p_data = function () {
        console.log("set p data");
    };
    Teacher.prototype.set_emp_data = function () {
        console.log("set emp data");
    };
    return Teacher;
}());
var c1 = new Teacher;
c1.set_p_data();
c1.set_emp_data();
