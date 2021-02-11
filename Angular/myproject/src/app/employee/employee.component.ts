import { Component, OnInit } from '@angular/core';
import {NgForm, MaxLengthValidator} from "@angular/forms"
import {department} from "../model/department.model"

@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {
    fullname:string;
    email:string;
    password:string;
    age:number;
    gender:string;
    isActive:boolean;
    department:string;

    dept:department[]=[
      {id:101,name:'python'},
      {id:102,name:'django'},
      {id:103,name:'api'},
      {id:104,name:'java'},
    ]

  constructor() { }

  ngOnInit(): void {
  }
  saveemp(empForm:NgForm):void
  {
    console.log(empForm);
  }

}
