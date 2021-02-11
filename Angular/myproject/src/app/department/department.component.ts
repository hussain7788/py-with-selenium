import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router'

@Component({
  selector: 'app-department',
  templateUrl: './department.component.html',
  styleUrls: ['./department.component.css']
})
export class DepartmentComponent implements OnInit {

  constructor( private router:Router) { }

  ngOnInit(): void {
  }
  department:any[]=[
    {id:101,name:'hussain',salary:100000},
    {id:102,name:'valli',salary:200000}
  ]
  
  onselect(x)
  {
    this.router.navigate(['/dept',x.id])
  }

}
