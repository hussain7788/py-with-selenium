import { Component, ElementRef, HostListener, OnInit } from '@angular/core';
import { Router } from '@angular/router';
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
    isValid:boolean = false;
    isInvalid:boolean = false;

  constructor(private ser:CrudOpsServiceService, public router:Router, private ele:ElementRef) { }

  ngOnInit(): void {
    this.get_emp_data()
    this.ele.nativeElement.style.color = "pink"
  }
  @HostListener('keypress')
  keypress(){
    // debugger;
    console.log(this.ele.nativeElement.value);
    
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
        this.isValid = true
        this.isInvalid = false
        this.router.navigateByUrl("/")
        alert(`${this.name} Successfully Logged in...`)
      }
      else{
        this.isValid = false
        this.isInvalid = true
      }
    }
    }
  }

