import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EmpListComponent } from './emp-list/emp-list.component';
import { EmployeeComponent } from './employee/employee.component';
import { DepartmentComponent } from './department/department.component';
import { DeptDetailsComponent } from './dept-details/dept-details.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { BookticketComponent } from './bookticket/bookticket.component';



const routes: Routes = [
  {path:'',redirectTo:'/list',pathMatch:'full'},
  {path:'list',component:EmpListComponent},
  {path:'emp',component:EmployeeComponent},
  {path:'dept',component:DepartmentComponent},
  {path:'dept/:id',component:DeptDetailsComponent},
  {path:'Book',component:BookticketComponent},
  {path:'**',component:PageNotFoundComponent},
  
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingcomponents=[
  EmpListComponent,EmployeeComponent,DepartmentComponent,DeptDetailsComponent,PageNotFoundComponent,BookticketComponent,
]
