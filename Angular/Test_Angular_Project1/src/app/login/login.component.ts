import { Component, OnInit } from '@angular/core';
import { CrudOpsServiceService } from '../crud-ops-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

    name:any;
    designation:any;
    message:any;
    l_emps:any;

  constructor(private ser:CrudOpsServiceService) { }

  ngOnInit(): void {
    this.get_emp_data()
  }
  get_emp_data(){
    this.ser.getAllEmps().subscribe(res =>
      {
        this.l_emps = res;
      })
  }
  login(){
 
    for(let i=0; this.l_emps.length>i; i++ ){
      console.log("emp::", this.l_emps[i])
      if(this.name == this.l_emps[i].name && this.designation == this.l_emps[i].degn){
        this.message = "valid user"
      }
    }
    console.log("message::", this.message)
    }
  }

