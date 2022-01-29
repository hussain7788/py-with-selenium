import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { CustomPreloadingStrategyService } from './lazyload/custom-preloading-strategy.service';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';


const routes: Routes = [

// path : "method" this is root path to enter into angularMethodsModule after next paths will consider in angMethodRoutingModule paths
  {path:'method', 
  loadChildren:() => import('./angular-methods/angular-methods.module').then((m) => m.AngularMethodsModule),
},
// we should only load module here using loadchildren method ...
  {
    path:'lazyload',
    loadChildren:() => import('./lazyload/lazyload.module').then((m) => m.LazyloadModule),
  // for preload we need to use data like this ..and we need to access in service (custompreloadstrategy service)
    data:{preload:false}
  },

  {path:'',component:HeaderComponent},
  {path:'register',component:RegisterComponent},
  {path:'login',component:LoginComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
  // this is service to deal with preload modules ..
    preloadingStrategy:CustomPreloadingStrategyService
  })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
