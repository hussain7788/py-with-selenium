import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AngularMethodsRoutingModule } from './angular-methods-routing.module';
import { PipesComponent } from './pipes/pipes.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HeaderComponent } from './header/header.component';
import { ObservablesComponent } from './observables/observables.component';
import { DirectivesDirective } from './directives.directive';
import { TemplateDrivenFormsComponent } from './template-driven-forms/template-driven-forms.component';
import { ReactiveFormsComponent } from './reactive-forms/reactive-forms.component';
import { RouterGuardComponent } from './router-guard/router-guard.component';


@NgModule({
  declarations: [
    PipesComponent,
    HeaderComponent,
    ObservablesComponent,
    DirectivesDirective,
    TemplateDrivenFormsComponent,
    ReactiveFormsComponent,
    RouterGuardComponent
  ],
  imports: [
    CommonModule,
    AngularMethodsRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  exports:[PipesComponent]
})
export class AngularMethodsModule {
  constructor(){
    console.log("angular methods loaded");
    
  }
 }
