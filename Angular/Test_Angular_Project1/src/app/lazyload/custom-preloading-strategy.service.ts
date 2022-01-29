import { Injectable } from '@angular/core';
import { PreloadingStrategy, Route } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CustomPreloadingStrategyService implements PreloadingStrategy {

  constructor() { }
// preloadStrategy class we need to implement and preload method need to implement here..
  preload(route: Route, load: () => Observable<any>): Observable<any> {
      if(route.data && route.data['preload']){
        console.log("preload path is::", route.path);
        return load();
      }
      else{
        return null
      }
  }

}
