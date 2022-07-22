```
TODO: Compilation
```

# Components of Java
- javac - converts .java to .class bytecode
- java - executes program. Launches JVM and runs bytecode
- jar - packages files together
- javadoc - generates documentation

In Java 8 there was JDK and JRE. JRE was a subset of JDK that can run but cant compile. Now you can create executable jar that runs by itself instead with JRE.

```
java -version
openjdk version "18.0.1" 2022-04-19
OpenJDK Runtime Environment Homebrew (build 18.0.1+0)
OpenJDK 64-Bit Server VM Homebrew (build 18.0.1+0, mixed mode, sharing)

javac -version
javac 18.0.1
```

# Classes
- Class - building block
- Object - runtime instance of class in memory
- Instance - single representation of class
- Reference - variable that points to an object

Class contains `members` of class. 
1. Fields - variables. Holds state. 
2. Methods - functions, procedures. Operates on state.
```
public class Animal {
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```
Method name `setName` and parameter type `String` are called `method signature`.

In this example method signature is `numberVisitors(int)`;
```
public int numberVisitors(int month) {
    return 10;
}
```
Usually one .java file has one class. But a .java file can define multiple classes. If multiple classes are present in file than only one can be public (it doesnt have to be).
If a class is public than the file and class have to have same name.

## Comments
- `//` - single line comment
- `/* */` - multiline comment
- `/** @author */` - javadoc comment

# Running app using java and javac
If java class is entry point of program it must contain valid `main()` method.
Main method has to be public. It can look like this
```
public static void main(String[] args) {}
public static void main(String[] args) {}
public static void main(String... args) { // variable argument list}

// final is optional
public final static void main(final String[] args) {}
```
Class doesnt have to be public to be an entry point.

When running `java Zoo`, Zoo is the name of class not file.
```
public class Zoo {
    public static void main(String[] args) {
        System.out.println("Hello world");
    }
}

javac Zoo.java
java Zoo
```
if class is in package
```
package com.example.kotlinspring01;
class Zoo {
    public static void main(String[] args) {
        System.out.println("Hello world");
    }
}

javac com/example/kotlinspring01/Zoo.java
java com.example.kotlinspring01.Zoo.java
```
This will only run if you are one level outside of `.com` package.

## with arguments
```
class Zoo {
    public static final void main(final String[] args) {
        System.out.println(args[0]);
    }
}

javac Zoo.java
java Zoo bojan          // bojan
java Zoo "Honey sweet"  // bojan
java Zoo                // Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 
```

## Single-file source-code
Skipping compiling when running single java file. 
```
java Zoo.java Bronx Zoo
```

# Packages
Package `import java.lang.*` is already imported, doestn have to be specified.
Also classes that are in same package as working class dont have to be imported.
```
import java.util.*;
class Zoo {
    public static final void main(final String[] args) {
        Random rnd = new Random();
        System.out.println(rnd.nextInt(10));
    }
}
```
If you need to import 
```
import java.nio.file.Files;
import java.nio.file.Paths;
```
you can
```
import java.nio.file.Paths.*;
```
but cannot
```
import java.nio.*;
import java.nio.*.*;
```
One of the reason for packages is in case there are multiple classes with same name.
```
import java.sql.Date;
import java.util.*;
import java.sql.*;

class Zoo {
    public static final void main(final String[] args) {
        java.util.Date date = Date.valueOf("");
        Date dateSql = Date.valueOf("");
    }
}
```

## Multiple classes compile
```
package packagea;
public class ClassA {}

package packageb;
import packagea.ClassA;
public class ClassB {
    public static void main(String[] args) {
        ClassA a;
        System.out.println("Got it");
    }
}

/tmp/packagea/ClassA.java
/tmp/packageb/ClassB.java
cd /tmp

javac packagea/ClassA.java packageb/ClassB.java
javac packagea/*.java packageb/*.java
// * only works one single folder level, not recursivly

java packageb.ClassB
```
to specify directory for output
```
javac -- classes packagea/ClassA.java packageb/ClassB.java

java --cp classes packageb.ClassB
java --classpath classes packageb.ClassB
java --class--path classes packageb.ClassB
```

## Compiling with Jar files
```
java -cp ".;C:\temp\someOtherLocation;c:\temp\myJar.jar" myPackage.MyClass
java -cp ".:/tmp/someOtherLocation:/tmp/myJar.jar" myPackage.MyClass
java -cp "C:\temp\directoryWithJars\*" myPackage.MyClass

```

## Create jar file
```
jar --cvf myNewFile.jar .
jar --create --verbose --file myNewFile.jar .
```

## Ordering Elements in Class - PIC package; import; class
- package declaration `package abc;`
- import statements `import java.util.*;`
- top level declaration `public class Animal{}` - only this required
- Field declaration `int value;`
- Method declaration `void method()`

# Constructor
Code inside `{}` is called code block. If there arent enough corresponding braces its called `balanced parentheses problem` and wont compile.
Code outside of constructor wrapped in `{}` is called `instance initializers`. There are also `static instance initializers`. They are executed in order before execution of constructor,

There are 4 type of code blocks
- class definition
- method declaration
- inner block
- instance initializer
```
public class Chicken {
    int numEggs = 12; // initialize on line
    String name;

    {
        System.out.println("Before");
    }

    public Chicken() {
        System.out.println("Constructor");
        name = "Duke";
    }

    public void Chicken() {
        System.out.println("Not a constructor");
    }

    {
        System.out.println("After");
    }

    public static void main(String[] args) {
        Chicken chicken = new Chicken();
        // before
        // after
        // Constructor
    }
}
```
First instance initializers are called in order and at the end constructor is executed. 
But instance initializers cant call a class field, if class field is defined after instance initializer.
```
{ System.out.println(name); } // DOES NOT COMPILE
private String name = "Fluffy";
```

# Data Types
## Primitive types
8 types represent building blocks. Primitive is not object in Java, its single value in memory. String is not primitive, its object.
- boolean false
- byte 1 : -128->127
- short 4: -32768->32767
- int 5 (default for whole): -2,147,483,648->2,147,483,647
- long 5L: pow(-2, 63) -> pow(-2, 63)-1
- float 0.5f: n/a
- double 0.5 (default for decimal): n/a
- char: 0->65535. default \u0000 

Numberic types are signed and reserves one bit to cover negative range. Instead of 0->255. Its -128->127

Short and char are similar and can be autocasted. Short is signed, has negative. Char is unsigned and is only positive.
```
char s = 5;     // OK - autocast
short d = 'd';  // OK - autocast
char w = -5;    // Doesnt compile, cause negative
char q = d;     // Doesnt compile
```
## Number system
- octal, has 0 as prefix, numbers 0-7: `017`
- hexadecimal, has 0x or 0X as prefix, 0-9a-f: `0xFF`. case insensitive
- decimal number system. Basic 0-9
- binary, has 0B or 0b as prefix, 0-1: `0b10

## Literals and underscores
Use `_` to make it easier to read.
```
int million = 1000000;
int million = 1_0_0_0_000;

double notAtStart = _1000.00;
double notAtEnd = 1000.00_;
double notByDecimal = 1000_.00;
double annoyingButLegal = 1_00_0.0_0;
double reallyUgly = 1__________2;
// DOES NOT COMPILE
// DOES NOT COMPILE
// DOES NOT COMPILE
// Ugly, but compiles
// Also compiles
```

# Reference types
Primitive holds a value in memory where the variable is allocated. Reference doesnt contain value instead it point to object stored in memory via `pointer`.
Unlike other language Java cant access direct address in memory.
Objects can be accessed only via referece.

```
String greeting;
greeting = new String("How are you");
```

- Reference types usually start with capital letter (not required). 
- Reference types can call a method on object.
- Reference types can have null assigned. Primitives cannot
```
String reference = "hello";
int len = reference.length();
int bad = len.length(); // DOES NOT COMPILE

int value = null;
// DOES NOT COMPILE
String name = null;
```
## Working with Wrapper classes
Each primitive has corresponding class. Methods with parse*, return primitive. Methods with valueOf return wrapper object. But you can autocast also.
```
Boolean wrapper = Boolean.valueOf(true);
boolean primitive = Boolean.parseBoolean("true");

boolean wrapper = Boolean.valueOf(true);
```
Wrapper objects have also methods like
```
Double apple = Double.valueOf("200.99");
System.out.println(apple.byteValue());  // 56
System.out.println(apple.intValue());       // 200
System.out.println(apple.doubleValue());    // 200.99
```

Wrapper classes have static methods. As always you can access static methods via instance but IDE doesnt autofill.
```
Double.min(1, 2)
Double.min(1, 2)
Double.sum(1, 2)
```

# Defining Text Blocks
String blocks have incidental whitespace, and essential whitespace.
After first `"""` you have to go to new line.
```
"Java Study Guide"
    by Scot & Jeanne
    
String title1 = "\"Java Study Guide\"\n    by Scott & Jeanne";
System.out.println(title1);

String title2 = """
        "Java Study Guide"
            by Scott & Jeanne
        """;
System.out.println(title2);

String block = """
    "doe\"\"\"
    \"deer\"""
    """;
System.out.print("*"+ block
        + "*");
* "doe"""
"deer"""
*
```

# Variables
Variable is name of piece of memory where data is stored.
```
## initializing variable
String zooName = "The Best Zoo";
```
## Identifier name rules
- Identifiers must begin with a letter, currency symbol or `_`. Currency are `$ ¥ €`...
- Identifiers can contain a number but cant start with it.
- Single `_` is not allowed
- No reserved word
```
abstract assert boolean break byte
case catch char class const*
continue default do double else
enum extends final finally float
for goto* if implements import
instanceof int interface long native
new package private protected public
return short static strictfp super
switch synchronized this throw throws
transient try void volatile while
true false null
```

## Multivariable initialization 
```
String s1, s2;
String s3 = "yes", s4 = "no";
// 4 delcared, 2 initialized

int i1, i2, i3 = 0; 
// 3 declared, 1 initialized

int num, String value; // DOES NOT COMPILE
```

Invalid valid declarations
```
boolean b1, b2;         // valid
String s1 = "1", s2;    // valid
double d1, double d2;   // not. Even if same type, should not be defined multiple times
int i1; int i2;         // valid cause ;
int i3; i4;             // not. Cause ;
```

## Final Local Variables
```
final int y = 10;
int x = 20;
y = x + 10; // DOES NOT COMPILE final

final int[] numbers = new int[10];
numbers[0] = 10;
numbers[1] = 10;
numbers = null; // DOES NOT COMPILE final
```

## Uninitialized Local Variables
```
public int notValid() {
    int y = 10;
    int x;
    int reply = x + y; // DOES NOT COMPILE
    return reply;
}
public int valid() {
    int y = 10;
    int x; // x is declared here
    x = 3; // x is initialized here
    int z; // z is declared here but never initialized or used
    int reply = x + y;
    return reply;
}

public void findAnswer(boolean check) {
    int answer;
    int otherAnswer;
    int onlyOneBranch;
    if (check) {
        onlyOneBranch = 1;
        answer = 1;
    } else {
        answer = 2; 
    }
    System.out.println(answer);
    System.out.println(onlyOneBranch); // DOES NOT COMPILE
}

public void checkAnswer() {
    boolean value;
    findAnswer(value); // DOES NOT COMPILE
}
```

## Instance and class variables
Instance variable, called a field is within instance of object.
Both defined on class level, but class variable is static.

## Inferring Type with var
Its local variable type inference. Works only on local variables. Not class
```
public class Zoo {
    public void whatTypeAmI() {
        var name = "Hello";
        var size = 7;
    }
}

public class VarKeyword {
    var tricky = "Hello"; // DOES NOT COMPILE
}
```
Also you cannot change type of var variable like in Javascript. Its fixed in runtime.
```
public void reassignment() {
    var number = 7;
    number = 4;
    number = "five"; // DOES NOT COMPILE
}
```
### Tricks with var
```
public void doesThisCompile(boolean check) {
    var question;       // DOES NOT COMPILE
    question = 1;
    var answer;         // DOES NOT COMPILE
    if (check) {
        answer = 2;
    } else {
        answer = 3;
    }
    System.out.println(answer);
}
    
public void twoTypes() {
    int a, var b = 3;   // DOES NOT COMPILE
    var n = null;       // DOES NOT COMPILE
}

public int addition(var a, var b) { // DOES NOT COMPILE
    return a + b;
}
```
weirdly this is allowed. But you cannot call class `var`. `Var is ok`.
```
package var;
public class Var {
    public void var() {
        var var = "var";
    }
    public void Var() {
        Var var = new Var();
    }
}
```
var is not allowed for compaund declaration
```
var a = 0, b=1;
```

## Variable scopes
- Local variables - in declaration until end of block
- Method params - In scope for entire method
- Instance variables - In scope until object until eligible for garbage collector
- Class variables - In scope until program ends

```
public void eatIfHungry(boolean hungry) {
    if (hungry) {
        int bitesOfCheese = 1;
        {
            int sss = 1;
            var teenyBit = true;
            System.out.println(teenyBit);
        }
        {
            int sss = 1;
        }
    }
    System.out.println(teenyBit); // DOES NOT COMPILE
}

// Compiles
public class Mouse {

final static int MAX_LENGTH = 5;
int length;
        public void grow(int inches) {
        if (length < MAX_LENGTH) {
            int newSize = length + inches;
            length = newSize;
        }
    }
}
```

# Destroying objects
Java has garbage collector in JVM. JVM is a platform which contains processes independant of your application.
Java objects are stored in heap memory (free store). Garbage collection is automatic process of freeing heap by deleting objects that are no longer reachable.
Eligible for garbage collection refers to an object state no longer accessible in program.
Objects are not immediately deleted. You can suggest to JVM to activate garbage collection, but not forcibly execute it.
```
System.gc()
```

