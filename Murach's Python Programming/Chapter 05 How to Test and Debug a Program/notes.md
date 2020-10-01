# Murach's Python Programming -- Chapter 5

- oh boy, a chapter on debugging!
- I'm going to try to write notes for this without a sarcastic tone
- rule #1: the purpose of TESTING is to make the program FAIL
- three types of errors
  - syntax errors: simple things like misspellings, etc. Will prevent script from running.
  - runtime errors: they don't break syntax rules, but still throw an exception that prevents the script from executing. These, along with syntax errors, are the easiest to fix.
  - Logic errors: these are errors that allow the script to run, but you've programmed it to do something other than what you want it to do. It's all your fault. SHAME. SHAME. SHAME!
- normally, you first test a program with valid data, then test it with anything invalid you can come up with
- The native Python IDE (IDLE) doesn't have a trace function, so you do it the old-fashioned way: with print() statements
- you can use the IDLE shell to test individual functions by typing them into the interactive prompt
- Strangely, IDLE does have a native debugger even without a trace feature. You can right-click on a line to set or get rid of a break point for the debugger.
- Go to Debug -- Debugger to open the debug control window.
- Press "Go" in this window in order to run the debugger, line by line. Most of the buttons are self-explanatory.
  - Go: run the program until hitting the breakpoint
  - step: step through code one line at  time, including statements in functions
  - over: step through code one line at a time, but skip evaluating the functions--just run them and assume they're okay
  - out: finish executing current function and return to calling function
  - quit: end it all
- if it might be helpful to view the program stack, go to Debug-->Stack Viewer from the IDLE window.
- Given that this is all very elementary--even moreso than what's been covered so far--I won't be doing the exercises at the end of the chapter. 



