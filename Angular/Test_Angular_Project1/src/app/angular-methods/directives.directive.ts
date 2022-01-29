import { Directive, OnInit, ElementRef, HostListener } from '@angular/core';

@Directive({
  selector: '[appDirectives]'
})
export class DirectivesDirective implements OnInit {

  constructor( private ele:ElementRef) { }

  ngOnInit(): void {
    debugger;
    this.ele.nativeElement.style.color = "yellow"
      
  }
  @HostListener('keyPress')
  keyPress(){
    console.log("element on key press:::", this.ele.nativeElement.value);
    
  }


}
