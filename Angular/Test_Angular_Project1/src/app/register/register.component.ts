import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, NgForm, Validators } from '@angular/forms';
import { CrudOpsServiceService } from '../crud-ops-service.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  name:any;
  designation:any;
  salary:any;
  formdata:any;
  id:any;
  emp_list:any;
  result:any;
  emp_data:any;
  updateFalse:any;
  message:any;
  emp_update:boolean = false

  data:any[]=[
    {id:1,name:"hussain", age:23},
    {id:2,name:"valli", age:24},
    {id:1,name:"ramu", age:25},
  ]

  constructor(private ser:CrudOpsServiceService) { }

  ngOnInit(): void {
    this.get_all_emps();
    for(let i of this.data){
      console.log("array data::", i.name);
      
    }
    const dt = this.data.map((value, index) =>{
      console.log(value.name, index);
      
    })

  }
  get_all_emps(){
    this.ser.getAllEmps().subscribe(res =>
      {
        this.emp_list = res;
        console.log("gettting data::", this.emp_list)
      })
  }
  saveEmp(empForm:NgForm){

    this.formdata = {id:this.id, name:this.name, degn:this.designation, salary:this.salary}
    console.log("empForm data:::", empForm.form)
    this.formdata = {id:empForm.value.id, name:empForm.value.name, degn:empForm.value.designation, salary:empForm.value.salary}

    this.ser.saveEmp(this.formdata).subscribe(res => {
      this.result = "Employee Added Successfully"
      this.get_all_emps();
      console.log("saved data:::", res)
    })
    
  }
  
  delete_emp(id:number){
    this.ser.deleteEmp(id).subscribe(res =>
      {
        this.get_all_emps();
        this.message = "User Deleted Successfully..."
       })
  }
  update_emp(id:number){
    this.ser.getEmp(id).subscribe(res =>{
      this.emp_data = res
      console.log("emp_data:::", this.emp_data)
      this.id = this.emp_data.id
      this.name = this.emp_data.name
      this.designation = this.emp_data.degn
      this.salary = this.emp_data.salary
    }) 
    // this.emp_update = true
  }
  updateEmpForm(empUpdateForm: NgForm){
    this.formdata = {id:empUpdateForm.value.id, name:empUpdateForm.value.name, degn:empUpdateForm.value.designation, salary:empUpdateForm.value.salary}
    this.ser.updateEmp(empUpdateForm.value.id, this.formdata).subscribe(res => {
      this.get_all_emps();
    })
    this.message = "User updated Successfully..."
    this.emp_update = false
  }
  

}
