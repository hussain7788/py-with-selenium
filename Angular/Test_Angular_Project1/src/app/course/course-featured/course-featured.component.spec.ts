import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CourseFeaturedComponent } from './course-featured.component';

describe('CourseFeaturedComponent', () => {
  let component: CourseFeaturedComponent;
  let fixture: ComponentFixture<CourseFeaturedComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CourseFeaturedComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CourseFeaturedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
