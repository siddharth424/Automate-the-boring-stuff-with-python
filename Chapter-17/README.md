### Chapter-17
##### 1. What is the Unix epoch?
It is a reference time. January 1, 1970, UTC.

##### 2. What function returns the number of seconds since the Unix epoch?
time.time()

##### 3. How can you pause your program for exactly 5 seconds?
time.sleep(5)

##### 4. What does the round() function return?
It rounds of the argument to closest integer.

##### 5. What is the difference between a datetime object and a timedelta object?
datetime represents a specific moment in time whereas timedelta represents duration of time or change in time.

##### 6. Using the datetime module, what day of the week was January 7, 2019?
datetime.datetime(2019,1,7).weekday()\
It returns 0 which is monday.

##### 7. Say you have a function named spam(). How can you call this function and run the code inside it in a separate thread?
```
threadobj = threading.Thread(target=spam)
threadobj.start()
```

##### 8. What should you do to avoid concurrency issues with multiple threads?
We should not read or write same variable by multiple threads.
