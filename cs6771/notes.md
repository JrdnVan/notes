# Introduction (Basic Types)

## Basic Keywords

### The auto keyword

```
int main(){
    ...
}

//can also be written as:

auto main() -> int {
    ...
}
```

```
// x = 4 and make object type same as 4 (int)
auto x = 4;

// y = 4.12 and make object type same as 4.12 (double)
auto y = 4.12;

CHECK(x < y);
```

### The const keyword

- The const keyword specifies that a **value can't** be modified (Immutable).
- Everything should be a const unless you know it'll be modified.

Some benefits:
- Compiler can see the const keyword and optimize knowing that the type of the value is const.
- Peace of mind
- Clearer code

```
auto const x = 4;
auto const y = 4.12;

//If string is constant, you can still append to string but can't change values within string.
auto const str = std::string("COMP6771");
```

### C++ has value semantics

Take for example the code below:

```
auto const hello = std::string("Hello");
auto hello2 = hello;

REQUIRE(hello == hello2); //true
hello2.append("2");
REQUIRE(hello != hello2); //true
```

### Boolean expressions

```
a && b //equivalent to
a and b

a || b //equivalent to
a or b

!a //equivalent to
not a
```

## Unit testing in C++

### Catch2

catch2 is a library in C++ which allows for unit testing.

```
#include <catch2/catch.hpp>
```

Basic example:
```
TEST_CASE("Types){
    SECTION("Numbers"){
        auto const x = 4;
        auto const y = 4;
        CHECK(x == y);
    }
    SECTION("Text"){
        ...
    }
}
```

### Require

- Require is like an assert, but doesn't terminate program when expression equals to false.

## Compiling

### clang

A modern compiler

```
clang++-11 filename.cpp
./a.out

clang++-11 filename.cpp -o filename
./filename
```

# C++ Basics

### Type Conversion

C++ allows for the converison of types implicitly and explicitly.

Take for example the code below:
```
auto const i = 2;
auto d = 1;

d = i; //Implicit
auto const d = static_cast<double>(i); //Explicit
```

### Default Arguments

- Functions can use default arguments, which is used if an actual argument is not specified when a function is called.
- Formal parameters: Those that appear in function definition.
- Actual parameters(arguments): Those that appear when calling function.

### Function Overloading

- Refers to a family of functions in the **same scope** that have the **same name** but **different formal parameters**.

```
auto square(int const x) -> int {
    return x * x;
}

auto square(double const x) -> double {
    return x * x;
}
```

### Switch-Statement

```
auto is_digit(char const c) -> bool {
    switch(c){
        case '0': [[fallthrough]];
        case '1': [[fallthrough]];
        case '2': [[fallthrough]];
        case '3': [[fallthrough]];
        case '4': [[fallthrough]];
        case '5': [[fallthrough]];
        case '6': [[fallthrough]];
        case '7': [[fallthrough]];
        case '8': [[fallthrough]];
        case '9': return true;
        default: return false;
    }
}
```

### References and const

- A reference to const means you can't modify the object using the reference.
- Object is still able to be modified, just not through the reference.
- Try to pass arguments by reference (Faster speeds as passing by value will create a copy of it)
  - May be able to get away with int, doubles, etc.

### Range-for-statements

```
for(auto const &x : vector){
    ...
}
```

### User-defined types

#### Enumerations

```
enum class computing_courses {
    intro,
    ds,
    cpp,
};

//usage
auto const x = computing_courses::intro;
```

#### Structures

```
struct name {
    int x;
    int y;
};

//init
auto const vals = name{
    .x = 1,
    .y = 2,
}
```

##### Checking if two struct objects are equal

```
auto operator==(name const&) const -> bool = default;
```

### Hash sets

```
auto name = absl::flat_hash_set<std::string>{
    "hello",
    "world",
};

//usage
name.contains("hello"); //true

name.insert("1");
name.erase("1");
name.clear(); //clear set
name.empty() //bool val
```

### Hash maps

### Declarations vs Definitions

- Declaration: makes known the type and name of a variable.
- Definition: a declaration, but also:
  - a variable definition allocates storage for, and constructs a variable.
  - A class definition allows you to create variables of the class' type.
  - You can call functions with only a declaration, but most provide definition later.
- Everything must have precisely one definition.

### Program Errors

Some program errors:

#### Compile-time Errors

```
auto main() -> int {
    a = 5; //no type specified.
}
```

#### Link-time Errors

```
auto is_cs6771() -> bool;
CHECK(is_cs6771()) //Link-time error: is_cs6771 not defined.
```

#### Run-time Errors
- User thrown errors

```
pseudo:
    if can't open file:
        throw error
```

#### Logic Errors
- SEGFAULTS

```
auto const empty = std::string("");
CHECK(empty[0] == 'C'); //bad character access
```

