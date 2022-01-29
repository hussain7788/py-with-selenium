import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { CrudOpsServiceService } from 'src/app/crud-ops-service.service';
import { EmpServiceService } from '../emp-service.service';


export interface IEmployee{
  id:any;
  name:any;
  degn:any;
  salary:any;
}


@Component({
  selector: 'app-observables',
  templateUrl: './observables.component.html',
  styleUrls: ['./observables.component.css']
})

export class ObservablesComponent implements OnInit {
    emp_list:any;
    error_msg:any;
    empForm:FormGroup;
    successMsg:boolean = false
    success:any;
    failure:any;
    putEmpData:any;

  constructor(public res:EmpServiceService , private router:Router, 
    private fb:FormBuilder, private actRouter:ActivatedRoute, private ser:CrudOpsServiceService) { }

  ngOnInit(): void {
    this.empForm = this.fb.group({
      id:['', Validators.required],
      name:['', [Validators.required, Validators.minLength(3), Validators.maxLength(10)]],
      degn:['', [ Validators.required]],
      salary:['']
    })
    this.getEmployee();

    this.actRouter.paramMap.subscribe(params => {
      let empId = +params.get('id')
      if (empId)
      {
        this.getEmpById(empId);
        console.log("empId", empId);
        
      }
    })

  }
  getEmpById(id:number){
    this.ser.getEmp(id).subscribe(res =>{
      this.editEmpData(res);
      console.log("getEmpById::", res);
      
  })
}
  editEmpData(empdata:IEmployee){
    this.empForm.patchValue({
      id:empdata.id,
      name:empdata.name,
      degn:empdata.degn,
      salary:empdata.salary,

    });
    this.successMsg = true

  }
  onSubmit(){
    console.log("empForm::", this.empForm);
    console.log("empForm::", this.empForm.value);
    console.log("empForm::", this.empForm.get('name').touched);
    if(this.successMsg){
      this.ser.updateEmp(this.empForm.value.id, this.empForm.value).subscribe(res=>{
        console.log("put data of employee", res);
        this.getEmployee();
        
      })
    }
    else{
      this.ser.saveEmp(this.empForm.value).subscribe(res=> {
        console.log("posted data of emp:", res);
        
      })
      this.getEmployee();
    }
    

   
  }
  getEmployee(){
    this.res.getEmployeeByObs().subscribe( res =>{
      console.log("result:::", res)
      this.emp_list = res;
    }

    )
  }
  editEmp(id:number){
      this.router.navigate(['/method/emp', id])
  }
  // if we send url parameters we can access by using this methods
  getUrlParams(obj:any){
// we can get url params by using this method too
    console.log(this.actRouter.snapshot.params['id']);
    
    console.log("url params::", obj);
    console.log("snapshot params::", this.actRouter.snapshot.paramMap);
    
  }

}
