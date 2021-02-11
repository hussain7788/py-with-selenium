import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {FormsModule} from "@angular/forms";
import { EmployeeComponent } from './employee/employee.component';
import { EmpListComponent } from './emp-list/emp-list.component';
import { DepartmentComponent } from './department/department.component';
import { DeptDetailsComponent } from './dept-details/dept-details.component'
import{Router,RouterModule} from '@angular/router';
import {AppRoutingModule,routingcomponents} from './app-routing.module';
import { BookticketComponent } from './bookticket/bookticket.component';


@NgModule({
  declarations: [
    AppComponent,
    routingcomponents,
    BookticketComponent
    
],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    RouterModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
