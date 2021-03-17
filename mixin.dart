// class A {
//   String getMessage() => 'A';
// }

// class B {
//   String getMessage() => 'B';
// }

// class P {
//   String getMessage() => 'P';
// }

// class AB extends P with A, B {}

// class BA extends P with B, A {}

// void main() {
//   AB ab = AB();
//   print(ab is P);
//   print(ab is A);
//   print(ab is B);

//   BA ba = BA();
//   print(ba is P);
//   print(ba is A);
//   print(ba is B);
// }

// class A {
//   String getMessage() => 'A';
// }

// class B {
//   String getMessage() => 'B';
// }

// class P {
//   String getMessage() => 'P';
// }

// class AB extends P with A, B {}

// class BA extends P with B, A {}

// void main() {
//   String result = '';

//   AB ab = AB();
//   result += ab.getMessage();

//   BA ba = BA();
//   result += ba.getMessage();

//   print(result);
// }


abstract class Super {
  void method() {
    print("Super");
  }
}

class MySuper implements Super {
  void method() {
    // super.method();
    print("MySuper");
  }
}


void main(){
  MySuper mySuper = MySuper();
  mySuper.method();
}