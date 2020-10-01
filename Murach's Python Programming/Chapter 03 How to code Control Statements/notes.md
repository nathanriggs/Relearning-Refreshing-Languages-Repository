# Murach's Python Programming -- Chapter 3

- floating-point variables have special problems, so don't use equality operators on them; use > or <.

- relational operators -- pretty much the same as any other contemporary language

  - ==, !=, >, <, >=, <=

- order of precedence for logical operators: NOT, AND, OR

  - like usual, use parentheses to override

- sorting sequence in Python is a bit different than what I'm used to

  - first digits 0-9, then uppercase letters, then lowercase letters. What about non-character entitites?

- string.lower() returns lowercase form of string

- string.upper() returns upper case form

- if/then, elseif, and else statements are structured as thus:

  - if (boolean):

    - statements

  - elif (boolean)

    - statements

  - else

    - statements

  - again, spacing determines what code block a statement is in

  - the _pass_ statement is used when there are no other statements to put into the block yet; if statements must always have something in their blocks

  - According to the book, using not operators is bad practice. I guess I'll believe them as it relates to Python, but other languages kind of need it.

  - nested if statements work like in most every other high level language, save for the use of spacing instead of curly braces

    - that does mean that things can get unwieldy pretty quickly, in terms of line length. Thus, Python encourages the use of functions and modules rather than a lot of nesting (which is the next chapter, I think)

  - Python uses the while statement for most iterative implementations, as such:

    - choice = "y"
    - while choice.lower() != "n"
      - choice = input("Continue? (y/n)")
    - print("done!")

  - However, for loops do exist in the language, and are used to a variety of ends

  - One basic way to set up a for loop is:

    - for i in range(0,10):
      - print(i,"\n")
    - the range() function can either accept a single end value, with an implied starting point of 0, accept a starting point and an end point, or a starting point, end point, and step value

  - in any loop, the break statement (no parentheses), as expected, breaks out of the loop and moves to the next statement after the loop. Similarly, the continue statement returns to the beginning of the loop. Why these aren't designed as functions is beyond my pay grade.

    