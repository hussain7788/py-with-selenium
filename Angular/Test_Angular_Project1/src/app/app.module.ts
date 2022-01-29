import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CrudOpsServiceService } from './crud-ops-service.service';
import { RegisterComponent } from './register/register.component';
import { HttpClientModule } from '@angular/common/http';
import { HeaderComponent } from './header/header.component';
import { BannerComponent } from './banner/banner.component';
import { FooterComponent } from './footer/footer.component';
import { CourseModule } from './course/course.module';
import { LoginComponent } from './login/login.component';
import { AngularMethodsModule } from './angular-methods/angular-methods.module';
import { EmpServiceService } from './angular-methods/emp-service.service';
import { LazyloadModule } from './lazyload/lazyload.module';
import { CustomPreloadingStrategyService } from './lazyload/custom-preloading-strategy.service';
import { AuthGuardGuard } from './angular-methods/router-guard/auth-guard.guard';

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    HeaderComponent,
    BannerComponent,
    FooterComponent,
    LoginComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    CourseModule,
    // AngularMethodsModule,
    ReactiveFormsModule,
  // if we want to lazyload any module then we should not import module here..
    // LazyloadModule,

  ],
  providers: [CrudOpsServiceService, EmpServiceService, CustomPreloadingStrategyService, AuthGuardGuard ],
  bootstrap: [AppComponent]
})
export class AppModule { 
  constructor(){
    console.log("app.module.ts loaded");
    
  }
}
