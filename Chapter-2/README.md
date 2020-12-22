### Chapter - 2
###### 1. What are the two values of the Boolean data type? How do you write them?
True and False.
It is written with its first letter in uppercase followed by lowercase. 

###### 2. What are the three Boolean operators?
a)and</br>
b)or</br>
c)not</br>

###### 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
&nbsp;

| A | B | A and B|
|:--:|:--:|:--:|
|False|False|False|
|False|True|False|
|True|False|False|
|True|True|True|

| A | B | A or B|
|:--:|:--:|:--:|
|False|False|False|
|False|True|True|
|True|False|True|
|True|True|True|

| A | not A |
|:--:|:--:|
|False|True|
|True|False|


###### 4. What do the following expressions evaluate to?
```python
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
```
False</br>
False</br>
True</br>
False</br>
False</br>
True</br>

###### 5. What are the six comparison operators?
a) ==</br>
b) !=</br>
c) ></br>
d) <</br>
e) >=</br>
f) <=

###### 6. What is the difference between the equal to operator and the assignment operator?
== is a comparison operator,it returns boolean value after comparision whereas = is assignment operator which is used to assign value to a variablea. 

###### 7. Explain what a condition is and where you would use one.
Condition is an expression which gives True or False. It is used for decision making.

###### 8. Identify the three blocks in this code:
&nbsp;
```python
spam = 0 
if spam == 10:
    print('eggs')#block-1 
    if spam > 5:
        print('bacon') #block-2
    else:
        print('ham') #block-3
    print('spam')
print('spam')
```


###### 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
&nbsp;
```python
spam=int(input())
if spam ==1 :
    print('Hello')
elif spam ==2:
    print('Howdy')
else:
    print('Greetings!')

```

###### 10. What keys can you press if your program is stuck in an infinite loop?
ctrl+c

###### 11. What is the difference between break and continue?
'break' is used to break out of loop whereas 'continue' is used to skip rest of the code for current iteration. 

###### 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
&nbsp;
|Range|values|argument|
|:------:|:-------:|:-----:|
|range(10)|0<=value<10|stop|
|range(0,10)|0<=value<10|start,stop|
|range(0,10,1)|0<=value<10|start,stop,step|

###### 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
&nbsp;
```python
for i in range(1,11):
    print(i)
```
```python
i=1
while(i<=10):
    print(i)
    i+=1
```

###### 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
spam.bacon()
