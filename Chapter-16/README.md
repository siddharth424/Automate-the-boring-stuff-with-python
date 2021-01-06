### Chapter-16
##### 1. What are some features Excel spreadsheets have that CSV spread-sheets don’t?
Excel spreadsheets have values of different data types whereas CSV only has strings.\
Excel spreadsheets have settings for font size and color, unlike CSV.\
Excel spreadsheets have multiple worksheets.\
Size of cell in Excel spreadsheets can be changed but not in CSV.\
Cells can be merged in Excel spreadsheets.\
Excel spreadsheets can have images or charts embedded in them but CSV don't.

##### 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?
File object which is returned by open().

##### 3. What modes do File objects for reader and writer objects need to be opened in?
reader objects - 'rb'(read binary)\
writer objects - 'wb'(write binary)

##### 4. What method takes a list argument and writes it to a CSV file?
writerow()

##### 5. What do the delimiter and lineterminator keyword arguments do?
delimiter argument is the string that appears between cells on a row.\
lineterminator argument is the string that comes at the end of a row.

##### 6. What function takes a string of JSON data and returns a Python data structure?
json.loads()

##### 7. What function takes a Python data structure and returns a string of JSON data?
json.dumps()
