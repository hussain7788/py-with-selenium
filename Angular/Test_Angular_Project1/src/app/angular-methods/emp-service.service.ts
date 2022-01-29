import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {IEmployee} from './observables/observables.component'


const url = "http://localhost:3000/emp/"
@Injectable({
  providedIn: 'root'
})
export class EmpServiceService {

  constructor(private http:HttpClient) { }

  getEmployeeByObs():Observable<IEmployee[]>{
    // debugger;
    return this.http.get<IEmployee[]>(url)

  }
  

}
