import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RouterGuardComponent } from './router-guard.component';

describe('RouterGuardComponent', () => {
  let component: RouterGuardComponent;
  let fixture: ComponentFixture<RouterGuardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RouterGuardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RouterGuardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
