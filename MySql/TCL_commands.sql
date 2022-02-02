use joins;
----- set transaction will store in buffer data rather than original database -----
start transaction;
insert into emp values(5,"chinna", 20000),(6,"somu", 30000);
--- end------

----- commit to save changes permanently.. once u commit we cant rollback again  ----
commit;
--- end ---------------

----- rollback used to back the started transactions ------
rollback;
---- end ----

delete from emp where eno=5;
set sql_safe_updates = 0;

----- savepoint used to save changes in buffer data -----
----- we can rollback perticular savepoint if we want -----

start transaction;
savepoint p1;
delete from emp where eno=1;
savepoint p2;
delete from emp where eno=2;
savepoint p3;
delete from emp where eno=3;

rollback to p3;
rollback to p2;
rollback to p1;

----- end ---------------------------------

start transaction;
savepoint m1;
insert into emp values(1,"hussain", 30000, 23);
savepoint m2;
insert into emp values(2,"valli", 40000, 24);
savepoint m3;
insert into emp values(3,"ramu", 50000, 25);

rollback to m3; 
rollback to m2;
rollback to m1;  
