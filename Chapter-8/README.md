### Chapter-08

##### 1. Does PyInputPlus come with the Python Standard Library?
No
##### 2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?
pyip is easier to type.
##### 3. What is the difference between inputInt() and inputFloat()?
inputInt() returns integer,whereas inputFloat() returns float value.
##### 4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?
Using pyip.inputInt(min=0,max=99)
##### 5. What is passed to the allowRegexes and blockRegexes keyword arguments?
List of regex strings.
##### 6. What does inputStr(limit=3) do if blank input is entered three times?
RetryLimitException is generated by the function.
##### 7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?
It will return 'hello'.
