import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-bookticket',
  templateUrl: './bookticket.component.html',
  styleUrls: ['./bookticket.component.css']
})
export class BookticketComponent implements OnInit {
    sno:string;
    from:string;
    to:string;
    dep_time:string;
    arr_time:string;
    capacity:number;
    select:string;

    travel:any[]=[
      {sno:1,travel:'SVR'},
      {sno:2,travel:'PVR'},
      {sno:3,travel:'JAGAN TRAVELS'},
      {sno:4,travel:'YATRA'},
      {sno:5,travel:'ARUNA TRAVELS'}
    ]

  constructor() { }

  ngOnInit(): void {
  }
  booktickets(bk:NgForm)
  {
    console.log(bk)
  }

}
