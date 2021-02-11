import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Employee } from './model/employee.model';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'myproject';
  constructor(private router:Router){}

  
}
