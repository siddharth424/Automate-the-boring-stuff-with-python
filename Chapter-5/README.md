#### Chapter-5
###### 1. What does the code for an empty dictionary look like?
{}

###### 2. What does a dictionary value with a key 'foo' and a value 42 look like?
{'foo':42}

###### 3. What is the main difference between a dictionary and a list?
The items of list are ordered whereas in dictionary they are not ordered

###### 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
It shows keyerror.

###### 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
There is no difference. 'cat' in spam is essentially a shorter version of writing 'cat' in spam.keys().

###### 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
'cat' in spam checks for a key named 'cat' whereas 'cat' in spam.values() checks whether there exists a key with value 'cat'.

###### 7. What is a shortcut for the following code?
```python
if 'color' not in spam:
    spam['color'] = 'black'
```

```python
spam.setdefault('color','black')
```

###### 8. What module and function can be used to “pretty print” dictionary values?
pprint.pprint()</br>
pprint module and pprint() function can be used.
