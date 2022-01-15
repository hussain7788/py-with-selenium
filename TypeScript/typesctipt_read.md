1. interfaces:-interface is a type which consists of public abstract methods and variables
   interface methods must implement in Derived class
2. By using interfaces we can achive Multiple Inheritance
3. By using interfaces we can achive Loosly coupling

4. abstract class:- abstract class must declare with abstract keyword
   abstract class consists of concrete methods and abstract methods
   concrete method :- method with body is called as concrete method
   concrete method is implemented method
   abstract method:- method without body is called as abstract method
   abstract method is unimplemented metho
   abstract method must implement in derived class
   ##########################
   class interface abstract class
   { { {
   variables declare variables variables
   concrete methods abstract methods concrete methods
   constructors } abstract methods
   static methods constructors
   } static methods
   }
   ##########################
   we cannot create object for abstract class or interface
   but we can create reference

5. interface is used to achieve multiple Inheritance
   multiple Inheritance means creating a derived class by using multiple base classes
   Typescript doesnot support multiple inheritance by using classes
   we can achive multiple inheritance by using interfaces
   Q)why Typescript doesnot support Doesnot support multiple inheritance by using classes?
   class A class B
   { {
   Show():void Show():void
   { {
   i am A show i am B Show
   } }
   } }
   class C extends A,B This program will not workin typescript
   {

   }
   observation:- in the above program same method exist in both the base classes
   because of inheritance these 2 methods are available in Derived class
   with derived class object and Reference if we access Show() then an ambiguity problem will
   occur that which method must gets executed
   inorder to overcome the above ambiguity problem Typescript doesnot support multiple
   inheritance by using classes
