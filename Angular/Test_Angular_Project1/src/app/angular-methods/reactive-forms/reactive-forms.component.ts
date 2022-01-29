import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormBuilder,Validators, NgForm } from '@angular/forms';

@Component({
  selector: 'app-reactive-forms',
  templateUrl: './reactive-forms.component.html',
  styleUrls: ['./reactive-forms.component.css']
})
export class ReactiveFormsComponent implements OnInit {
  employeeForm:FormGroup;
  lastName:any;
  skillOptions:any[]=[
    {name:"python"},
    {name:"java"},
    {name:"angular"},
    {name:"php"}
  ]

  constructor(private fb:FormBuilder) { }
  get username(){
    return this.employeeForm.controls?.['firstName']
  }

  // formGroup method is collection of formControls ..
  //formGroup and formBuilder almost same 

  // ngOnInit(): void {
  //   this.employeeForm = new FormGroup({
  //     firstName : new FormControl(),
  //     email : new FormControl(),
  //     skills : new FormGroup({
  //       skillName:new FormControl(),
  //       exp:new FormControl(),
  //       proficiency:new FormControl(),
  //     })
  //   })
  // }

  //formBuilder is used when we work with complex validations 
  ngOnInit():void{
    this.employeeForm = this.fb.group({
      firstName:['', [Validators.required, Validators.minLength(2), Validators.maxLength(10)]],
      email:[''],
      skills:this.fb.group({
        skillName:[''],
        exp:[''],
        proficiency:['']

      })
    })
  }
  // to log firstname formGroup
  log(lastName:any){
    console.log("lastName:::",lastName);
    
  }
  // set value method 
  // set value method to set all values to fields 
  // if we want to set only 1 or 2 fields we can use {patchValue} method
  // patchValue method update all values without error like setValue method.
  loadData(){
    this.employeeForm.setValue({
      firstName:"hussain",
      email:"hussain5@gmail.com",
      skills: {
        skillName:"python",
        exp:"2",
        proficiency:"advanced"
      }
    })
  }
  onSubmit(){
    console.log(this.employeeForm)

    console.log(this.employeeForm.value)
    console.log(this.employeeForm.touched);
    console.log(this.employeeForm.controls?.['firstName'].touched);
    console.log(this.employeeForm.get('firstName').value);
    
  }
  saveForm(form:NgForm){
    console.log("form::", form);
    
  }
}
