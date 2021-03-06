# Murach's Python Programming -- Chapter 2

- indentation in python acts as curly braces in most other languages
- implicit continuation of a line is simply done by using a normal operator sign (+,-,etc.)
- explicit continuation notation done using a backslash at the end of the first line, but this is almost never necessary or recommended
- comments are indicated using the # sign. You can do this at the beginning of the line as a block comment or after a statement as an inline comment
- some very basic functions
  - str(x) = string value of x
  - int(x) = integer value of x
  - float(x) = floating-point value of x
  - bool(x) = boolean value of x (true or false)
  - round(x [,digits]) = rounds the floating number argument to the number of digits specified. If no digits are given, then it simply returns the nearest integer
- In Python, it is convention to name variables with spaces replaced by underscores
  - the exception to this is using Camel Case when Object-Oriented programming is being used
  - ultimately, just pick one and stick to it for the whole program
- Python Arithmetic Operators
  - \+ = addition
  - \- = subtraction
  - \* = multiplication
  - / = floating-point division
  - // = integer division
  - % = modulus / remainder
  - \** = exponentiation
- order of operations
- \** \* / // % + -, left to right
- compound assignment operators: +=, -=, *=, etc. Same as in most languages
- string concatenation is done with a plus sign, like in BASIC or javascript
- other functions introduced in this chapter:
  - print()
    - this can take multiple arguments
    - you can end arguments with a "sep=' | '" to indicate a separator
    - there is also "end='...'"
  - input()
    - all entries are returned as strings, so numbers have to be converted
    - the argument is the prompt of the input statement, and is optional