import { TestBed } from '@angular/core/testing';

import { CrudOpsServiceService } from './crud-ops-service.service';

describe('CrudOpsServiceService', () => {
  let service: CrudOpsServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CrudOpsServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
