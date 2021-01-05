### Chapter-11

##### 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
assert spam >= 10, 'spam is less than 10.'

#####  2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
assert eggs.lower() != bacon.lower(), 'eggs and bacon are same'

#####  3. Write an assert statement that always triggers an AssertionError.
assert False, 'AssertionError'

#####  4. What are the two lines that your program must have in order to be able to call logging.debug()?
```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
```

#####  5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
```python
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
```
#####  6. What are the five logging levels?
DEBUG, INFO, WARNING, ERROR, CRITICAL

#####  7. What line of code can you add to disable all logging messages in your program?
```python 
logging.disable(logging.CRITICAL)
```

#####  8. Why is using logging messages better than using print() to display the same message?
Logging messages can be removed by logging.disable() whereas for print() we have to remove each print statement. Also logging messages has timestamps.

#####  9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
Step In moves the debugger into function call. Step Over executes the function call without stepping into it. Step Out executes all the code until it steps out of it's current function.

#####  10. After you click Continue, when will the debugger stop?
The debugger stops when it reaches end of the progrom or breakpoint.

#####  11. What is a breakpoint?
A breakpoint causes the debugger to pause whenever the program execution reaches that line.

#####  12. How do you set a breakpoint on a line of code in Mu?
By clicking the line number.
