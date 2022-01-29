import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-pipes',
  templateUrl: './pipes.component.html',
  styleUrls: ['./pipes.component.css']
})
export class PipesComponent implements OnInit {

  public Sno:number=12345;
  public Sname:string="anilkumar";
  public Cname:string="SQLSERVER";
  public Emailid:string="abc.def@gmail.com";
  public JoinDate:Date=new Date();
  public Fees:number=4500;
  public CollegeName:string="sathyatechnologies";

  constructor() { }

  ngOnInit(): void {
  }

}
