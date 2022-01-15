import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CourseRoutingModule } from './course-routing.module';
import { CourseFeaturedComponent } from './course-featured/course-featured.component';


@NgModule({
  declarations: [
  
    CourseFeaturedComponent
  ],
  imports: [
    CommonModule,
    CourseRoutingModule
  ],
  exports:[CourseFeaturedComponent]
})
export class CourseModule { }
