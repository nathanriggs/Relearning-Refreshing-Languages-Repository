# Murach's Python Programming -- Chapter 4

- start the name of a function with a verb; this is best practice for most languages
- syntax for defining a function
  - def function_name([arguments]):
    - statement
    - statement
    - etc
- every program should have a main() function, even if it's a lit of modules or a library. The main() function in a library can test each function in the library, for instance, or explain what the library does.
- While the book doesn't make it *entirely* clear as to why this is, you should not simply call main() t the end of a program (though this makes sense in a library). Instead, you want to check if the current module is the main module, in which case then it would run the main() function. This is accomplished as such:
  - if \_\_name\_\_ == "_\_main\_\_":
    - main()
  - This will likely be explained in further detail once object-oriented programming is addressed in the book
  - passing parameters works mostly the same as in other high-level languages, with the exception of the fact that arrays are mutable, rather than immutable (most objects/variables are immutable). This means that a change to the array passed will change the global array itself; there is a deepcopy() function for arrays (called lists and tuples in Python). Chapter 6 covers this in more detail
  - DOCUMENTING A MODULE
    - this is actually an interesting feature of Python--finally!
    - you can create documentation for other programmers by using _docstrings_, which are paragraphs delimited by """ to begin and end the documentation. The end programmer can then type help _your_function_, and the documentation you place in between the """ delimeters will be displayed
  - importing modules
    - you simply use the import statement, followed by the module name
    - you can also import it as a different namespace as such:
      - import module1 as the_module
    - additionally,  you can import only specific functions to the global namespace as such:
      - from module1 import the_function
      - of course, global functions and variables are the spawn of satan in high level languages, so don't do this unless it's absolutely necessary
    - a list of some of the most-used standard modules in Python:
      - math--obviously, for math functions
      - random--PRNG functions
        - random.random() returns a float value between 0 and 1
        - random.randint(min, max) returns a random intenger between the min and max
        - random.randrange([start,] stop [,step]) returns a value greater than the start value and less than the stop value, while remaining a multiple of the step value
      - decimal--for working with fixed-point decimal numbers instead of floating point 
      - csv--for working with comma-separated-value files
      - pickle--for working with persistent data storage 
        - I am unsure at this point if this refers to databases, file IO, or something else
      - tkinter--functions for create GUI apps with the Tk interface



