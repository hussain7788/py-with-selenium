import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LazyloadRoutingModule } from './lazyload-routing.module';
import { Component1Component } from './component1/component1.component';


@NgModule({
  declarations: [
    Component1Component
  ],
  imports: [
    CommonModule,
    LazyloadRoutingModule
  ],
  exports:[Component1Component]
})
export class LazyloadModule { 
  constructor(){
    console.log("lazyload module loaded");
    
  }
}
