import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }
  isUserLoggedIn(){
    alert("not authenticated user")
    return false;
  }
}
