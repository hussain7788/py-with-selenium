import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HeaderComponent} from './header/header.component'
import { ObservablesComponent } from './observables/observables.component';
import { PipesComponent } from './pipes/pipes.component';
import { ReactiveFormsComponent } from './reactive-forms/reactive-forms.component';
import { AuthGuardGuard } from './router-guard/auth-guard.guard';
import { RouterGuardComponent } from './router-guard/router-guard.component';
import { TemplateDrivenFormsComponent } from './template-driven-forms/template-driven-forms.component';

const routes: Routes = [
    {path:"pipes", component:PipesComponent},
    {path:"", component:HeaderComponent},
    {path:"observables", component:ObservablesComponent},
    {path:"emp/:id", component:ObservablesComponent},
    {path:"tempDrivenForms", component:TemplateDrivenFormsComponent},
    {path:"reactiveForms", component:ReactiveFormsComponent},
  // this is authguard used to give access to perticular route and manage whether or not navigate to route
    {path:"routeGuard", component:RouterGuardComponent,canActivate:[AuthGuardGuard]},


// if we want parent path and child path we can do like this........
  // {path:"method", children:[
  //   {path:"pipes", component:PipesComponent},
  //   {path:"", component:HeaderComponent},
  //   {path:"observables", component:ObservablesComponent},
  //   {path:"emp/:id", component:ObservablesComponent},
  //   {path:"tempDrivenForms", component:TemplateDrivenFormsComponent},
  //   {path:"reactiveForms", component:ReactiveFormsComponent}
  // ]}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AngularMethodsRoutingModule { }
