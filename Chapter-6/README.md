### Chapter-06

###### 1. What are escape characters?
Escape characters are special characters in a string which otherwise would be impossible to insert.

###### 2. What do the \n and \t escape characters represent?
The '\n' is used for a new line.
The '\t' is used to create a tab in a string.
###### 3. How can you put a \ backslash character in a string?
'\\\\'
##### 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
Double quotes are used to represent the string so single quotes in Howl's does not make it invalid.
##### 5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
You could use multiline strings. Like this:
```
This a mulitline sting
It is created by three '`'

```
###### 6. What do the following expressions evaluate to?
```python
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
```
'e'\
'Hello'\
'Hello'\
'lo, world!'
###### 7. What do the following expressions evaluate to?
```python
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
```
.upper() changes 'Hello' to 'HELLO'
.upper().isupper() first converts 'Hello' to 'HELLO' then checks if all characters are upper case. Which is True.
.upper().lower() first converts 'Hello' to 'HELLO' and then converts 'HELLO' to 'hello'
###### 8. What do the following expressions evaluate to?
```python 
'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
```
['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']\
'There-can-be-only-one.'
###### 9. What string methods can you use to right-justify, left-justify, and center a string?
string.rjust()\
string.ljust()\
string.center()
###### 10. How can you trim whitespace characters from the beginning or end of a string?
 By using lstrip() and rstrip() methods we can remove the white spaces from the beginning or the end of a string.
