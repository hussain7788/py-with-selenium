import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourseFeaturedComponent } from './course-featured/course-featured.component';

const routes: Routes = [
  {path:'course',component:CourseFeaturedComponent},

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CourseRoutingModule { }
