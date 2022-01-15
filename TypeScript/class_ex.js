var Student = /** @class */ (function () {
    function Student() {
    }
    Student.prototype.get_student_data = function (rollno, address) {
        this.rollno = rollno;
        this.address = address;
        console.log("student college name is ".concat(Student.college, " rollno is ").concat(this.rollno, " address is ").concat(this.address));
    };
    Student.prototype.CalcMarks = function (marks_list) {
        var total = 0;
        console.log("marks_list", marks_list);
        for (var i = 0; marks_list.length > i; i++) {
            total += marks_list[i];
        }
        return total;
    };
    Student.prototype.getMarks = function () {
        var data = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            data[_i] = arguments[_i];
        }
        var t_marks = this.CalcMarks(data);
        console.log("total marks:", t_marks);
    };
    Student.college = "arts college";
    return Student;
}());
var s1 = new Student();
s1.get_student_data(122334, "kadapa");
s1.getMarks(10, 20, 30, 40, 50);
