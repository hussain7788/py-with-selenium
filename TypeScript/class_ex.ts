class Student{
    static college:string = "arts college";
    rollno:number;
    address:string;
    get_student_data(rollno:number, address:string):void{
        this.rollno = rollno
        this.address = address
        console.log(`student college name is ${Student.college} rollno is ${this.rollno} address is ${this.address}`)
    }
    CalcMarks(marks_list:any){
        var total:number = 0
        console.log("marks_list", marks_list)
        for (let i =0; marks_list.length>i; i++){
            total += marks_list[i]
        }
        return total
    }
    getMarks(...data:number[]){
        let t_marks = this.CalcMarks(data)
        console.log("total marks:", t_marks)
    }
}
let s1 = new Student()
s1.get_student_data(122334, "kadapa")
s1.getMarks(10,20,30, 40,50)