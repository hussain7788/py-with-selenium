import { Component, OnInit } from '@angular/core';
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

  constructor(private ser:CrudOpsServiceService) { }

  ngOnInit(): void {
    this.get_all_emps();
  }
  get_all_emps(){
    this.ser.getAllEmps().subscribe(res =>
      {
        this.emp_list = res;
        console.log("gettting data::", this.emp_list)
      })
  }
  save_emp(){
    this.formdata = {id:this.id, name:this.name, degn:this.designation, salary:this.salary}
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
      })
  }

}
