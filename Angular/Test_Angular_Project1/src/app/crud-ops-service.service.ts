import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CrudOpsServiceService {

  constructor(private http:HttpClient) { }
  saveEmp(formData:any){
    return this.http.post("http://localhost:3000/emp", formData)
  }

  getAllEmps(){
    return this.http.get("http://localhost:3000/emp/")
  }
  deleteEmp(id:number){
    return this.http.delete("http://localhost:3000/emp/" + id)
  }



}
