### Chapter - 4
###### 1. What is []?
It is an empty list.

###### 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
```python 
spam[2]='hello'
```

##### For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

###### 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
'd'

###### 4. What does spam[-1] evaluate to?
'd'

###### 5. What does spam[:2] evaluate to?
['a', 'b']

##### For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

###### 6. What does bacon.index('cat') evaluate to?
1

###### 7. What does bacon.append(99) make the list value in bacon look like?
[3.14, 'cat', 11, 'cat', True, 99]

###### 8. What does bacon.remove('cat') make the list value in bacon look like?
[3.14, 11, 'cat', True]

###### 9. What are the operators for list concatenation and list replication?
Operator for concatination is +
Operator for replication is *

###### 10. What is the difference between the append() and insert() list methods?
append() can only add value in end of the list whereas insert() can add it anywhere in the list by mentioning the position and element.

###### 11. What are two ways to remove values from a list?
del and remove()

###### 12. Name a few ways that list values are similar to string values.
Both have indexes and slices.
Both can be concatinated and replicated.

###### 13. What is the difference between lists and tuples?
In lists values can be modified,added or removed but in tuples elements cannot be changed.

###### 14. How do you type the tuple value that has just the integer value 42 in it?
t = (42,)

###### 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
By using tuple() to get in tuple form and by using list() to get in list form.

###### 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
They contain references to lists.

###### 17. What is the difference between copy.copy() and copy.deepcopy()?
copy.copy() does a shallow copy, it copies by reference.
copy.deepcopy() does a deep copy, it copies by value. 

