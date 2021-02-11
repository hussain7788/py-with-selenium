import { Component, OnInit } from '@angular/core';
import{ActivatedRoute, ActivationEnd}  from '@angular/router';

@Component({
  selector: 'app-dept-details',
  templateUrl: './dept-details.component.html',
  styleUrls: ['./dept-details.component.css']
})
export class DeptDetailsComponent implements OnInit {
  public departmentid;
  constructor(private route:ActivatedRoute) { }

  ngOnInit(): void {
    let id=parseInt(this.route.snapshot.paramMap.get('id'));
    this.departmentid=id;
  }


}
