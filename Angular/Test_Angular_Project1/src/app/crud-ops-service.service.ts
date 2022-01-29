import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IEmployee } from './angular-methods/observables/observables.component';

const url = "http://localhost:3000/emp/"
@Injectable({
  providedIn: 'root'
})
export class CrudOpsServiceService {

  constructor(private http:HttpClient) { }
  saveEmp(formData:any){
    return this.http.post(url, formData)
  }

  getAllEmps(){
    return this.http.get(url)
  }
  deleteEmp(id:number){
    return this.http.delete(url  + id)
  }

  getEmp(id:number):Observable<IEmployee> {
    return this.http.get<IEmployee>(url + id)
    // return this.http.get(url + id)
  }

  // getEmp(id:number){
  //   return this.http.get(url + id)
  //   // return this.http.get(url + id)
  // }
  updateEmp(id:number, formData:any){
    return this.http.put(url + id, formData)
  }



}
