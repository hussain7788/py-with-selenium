import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-emp-list',
  templateUrl: './emp-list.component.html',
  styleUrls: ['./emp-list.component.css']
})
export class EmpListComponent implements OnInit {


  employee:any=[
    {
      id:101,
      'name':'hussain',
      'salary':100000,
      'gender':'male',
      'email':'gangan@gmail.com',
      'photo':'assets/travel-1.png'

    },
    {
      id:102,
      'name':'valli',
      'salary':200000,
      'gender':'male',
      'email':'gangan3@gmail.com',
      'photo':'assets/download.png'

    }
  ]
  constructor() { }

  ngOnInit(): void {
  }

}
